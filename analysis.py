from os import path
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pydantic import BaseModel


class Analysis(BaseModel):
    df_cleaned: pd.DataFrame = None
    path: str
    
    class Config:
        arbitrary_types_allowed = True
    
    # Function to get the cleaned data and clean some fields for plotting
    def get_data(self):
        self.df_cleaned = pd.read_csv(self.path)
        # self.df_cleaned["trending_date"] = pd.to_datetime(self.df_cleaned["trending_date"], format="%Y-%d-%m")
        # self.df_cleaned["publish_time"] = pd.to_datetime(self.df_cleaned["publish_time"], format="%Y-%m-%dT%H:%M:%S.%fZ")
    
    # Univariate analysis
    # Plotting individual features to see how they behave and check if we need to normalise any data
    def univariate_analysis(self):
        numerical_columns = ["views", "likes", "dislikes", "comment_count", "like_ratio", "comment_ratio"]
        categorical_columns = ["category_name", "channel_title_cleaned", "region",  "trending_day", "trending_month", "publish_day", "publish_hour"]
        
        for col in numerical_columns:
            plt.figure(figsize=(10,6))
            sns.histplot(self.df_cleaned[col], kde=True)
            plt.title(f"Distribution of {col}")
            plt.xlabel(col)
            plt.ylabel("Frequency")
            plt.show()
            
            plt.figure(figsize=(8,5))
            sns.boxplot(x=self.df_cleaned[col])
            plt.title(f"Boxplot of {col}")
            plt.ylabel(col)
            plt.show()
        
        for col in categorical_columns:
            plt.figure(figsize=(12,6))
            sns.countplot(y=self.df_cleaned[col], order=self.df_cleaned[col].value_counts().index[:15]) # Top 15 categories channels
            plt.title(f"Top 15 {col}")
            plt.xlabel("Count")
            plt.ylabel(col)
            plt.show()

def main():
    yt_data_analysis = Analysis(path="./data/cleaned_data.csv")
    yt_data_analysis.get_data()
    yt_data_analysis.univariate_analysis()
    
if __name__ == "__main__":
    main()   