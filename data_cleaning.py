import pandas as pd
import json
import os
from pydantic import BaseModel
import re

class YoutubeDataAnalysis(BaseModel):
    path: str
    df_videos: pd.DataFrame = None
    all_category_data: dict = {}
    
    class Config:
        arbitrary_types_allowed = True
    # Prepare the data for the analysis
    def videos_data(self):
        concatinated_data = []

        for filename in os.listdir(self.path):
            if filename.endswith("videos.csv"):
                filepath = os.path.join(self.path, filename)
                country = filename.split("videos.csv")[0]
                try:
                    df = pd.read_csv(filepath)
                    df["region"] = country
                    concatinated_data.append(df)
                except:
                    df = pd.read_csv(filepath, encoding="utf-8")
                    df["region"] = country
                    concatinated_data.append(df)

        self.df_videos = pd.concat(concatinated_data, ignore_index=True)
        # print("Initial Video Dataframe info:")
        # self.df_videos.info()
        # Checking if all the data is loaded correctly
        contries = self.df_videos["region"].unique()
        # If you can see all the countries in the data, then it is loaded correctly
        print(f"Countries in the data: {contries}")

    # Prepare Category data for the analysis
    def category_data(self):
        for filename in os.listdir(self.path):
            if filename.endswith("_category_id.json"):
                filepath = os.path.join(self.path, filename)
                country = filename.split("_category_id.json")[0]
                with open(filepath, "r") as file:
                    data = json.load(file)
                    categories = categories = {item['id']: item['snippet']['title'] for item in data['items']}
                    self.all_category_data[country] = categories

    # Function to map category ID to category name
    def get_category_name(self, item):
        region = item["region"]
        category_id = str(item["category_id"])
        if region in self.all_category_data and category_id in self.all_category_data[region]:
            return self.all_category_data[region][category_id]
        return None
    
    # Handling missing values
    def handle_missing_values(self):
        self.df_videos.fillna("", inplace=True)
        numeric_columns = self.df_videos.select_dtypes(include=["float64", "int64"]).columns
        for col in numeric_columns:
            # Filling missing values with the mean of the column
            # Change if the code becomes too slow
            self.df_videos[col].fillna(self.df_videos[col].mean(), inplace=True)
    
    # Dropping duplicates
    def drop_duplicates(self):
        # It is not a good idea to drop data but if everything is duplicated in this case we can drop it for cleanliness
        # Drop duplicates based on all columns
        self.df_videos.drop_duplicates(inplace=True)
    
    # Cleaning text
    def clean_text(self, text):
        if isinstance(text, str):
            text = re.sub(r"[^a-zA-Z0-9\s]", "", text) # Remove special characters
            text = " ".join(text.split()) # Remove extra spaces
            # Convert to lowercase
            text = text.lower()
            return text
        return text
    
    def create_new_features(self):
        self.df_videos['trending_day'] = self.df_videos['trending_date'].dt.day_name()
        self.df_videos['trending_month'] = self.df_videos['trending_date'].dt.month_name()
        self.df_videos["publish_day"] = self.df_videos["publish_time"].dt.day_name()
        self.df_videos["publish_hour"] = self.df_videos["publish_time"].dt.hour
        self.df_videos["like_ratio"] = self.df_videos["likes"].astype(float) / (self.df_videos["dislikes"].astype(float) + 1) # Adding 1 to avoid division by zero
        self.df_videos["comment_ratio"] = self.df_videos["comment_count"].astype(float) / (self.df_videos["views"].astype(float) + 1) # Adding 1 to avoid division by zero
        
    # Data Cleaning and Preparation
    def data_cleaning(self):
        # Converting 'trending_date' to datetime
        self.df_videos["trending_date"] = pd.to_datetime(self.df_videos["trending_date"], format="%y.%d.%m")
        # Converting 'publish_time' to datetime
        self.df_videos["publish_time"] = pd.to_datetime(self.df_videos["publish_time"], format="%Y-%m-%dT%H:%M:%S.%fZ")
        self.df_videos["title_cleaned"] = self.df_videos["title"].apply(self.clean_text)
        self.df_videos["channel_title_cleaned"] = self.df_videos["channel_title"].apply(self.clean_text)
        
        
    def data_concatination(self):
        self.videos_data()
        self.category_data()
        self.df_videos["category_name"] = self.df_videos.apply(self.get_category_name, axis=1)
        self.handle_missing_values()
        # Dropping duplicates
        self.drop_duplicates()
        self.data_cleaning()
        self.create_new_features()
        print("*********************************")
        print(self.df_videos.loc[[0, 1, 2, 3, 4], ["title", "likes", "dislikes", "like_ratio"]])
    
        
def main():
    yt_data_analysis = YoutubeDataAnalysis(path="./data")
    yt_data_analysis.data_concatination()
    
if __name__ == "__main__":
    main()
