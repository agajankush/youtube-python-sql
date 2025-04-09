from os import path
from matplotlib import category
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pydantic import BaseModel


class Analysis(BaseModel):
    df_cleaned: pd.DataFrame = None
    path: str
    numerical_columns: list = []
    categorical_columns: list = []
    
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
        for col in self.numerical_columns:
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
        
        for col in self.categorical_columns:
            plt.figure(figsize=(12,6))
            sns.countplot(y=self.df_cleaned[col], order=self.df_cleaned[col].value_counts().index[:15]) # Top 15 categories channels
            plt.title(f"Top 15 {col}")
            plt.xlabel("Count")
            plt.ylabel(col)
            plt.show()

    # Bivariate Analysis
    # Plotting the relationship between two features
    def bivariate_analysis(self):
        # Numerical vs Categorical
        print("Numerical vs Categorical")
        plt.figure(figsize=(15,8))
        sns.boxplot(x="category_name", y="views", data=self.df_cleaned)
        plt.title("Boxplot of Views by Category")
        plt.xlabel("Category")
        plt.ylabel("Views")
        plt.xticks(rotation=45, ha="right")
        plt.show()
        
        plt.figure(figsize=(15,8))
        sns.violinplot(x="region", y="likes", data=self.df_cleaned)
        plt.title("Violinplot of Likes by Region")
        plt.xlabel("Region")
        plt.ylabel("Likes")
        plt.xticks(rotation=45, ha="right")
        plt.show()
        
        # Correlation matrix
        correlation_matrix = self.df_cleaned[self.numerical_columns].corr()
        plt.figure(figsize=(12,8))
        sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
        plt.title("Correlation Matrix of Numerical Features")
        plt.show()
    
    # Analyze trends over time
    def analyze_trends_over_time(self):
        # Convert trending_date to datetime
        # self.df_cleaned["trending_date"] = pd.to_datetime(self.df_cleaned["trending_date"], format="%Y-%d-%m")
        
        # Group by trending_date and sum the views
        daily_trends = self.df_cleaned.groupby("trending_date")[["views", 'likes', 'comment_count']].sum()
        
        plt.figure(figsize=(15,6))
        plt.plot(daily_trends.index, daily_trends["views"], label="Views", color="blue")
        plt.plot(daily_trends.index, daily_trends["likes"], label="Likes", color="black")
        plt.plot(daily_trends.index, daily_trends["comment_count"], label="Total Comments", color="green")
        plt.title("Daily Trends of Views, Likes, and Comments")
        plt.xlabel("Trending Date")
        plt.ylabel("Count")
        plt.xticks(rotation=45, ha="right")
        plt.show()
        
        # Analyze trending frequency of categories over time
        category_trends = self.df_cleaned.groupby(["trending_date", "category_name"]).size().unstack(fill_value=0)
        plt.figure(figsize=(18,10))
        category_trends.plot(kind='line', legend='reverse')
        plt.title("Trending Frequency of Categories Over Time")
        plt.xlabel("Trending Date")
        plt.ylabel("Number of trending videos")
        plt.legend(title="Category", bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        plt.show()
    
def main():
    numerical_columns = ["views", "likes", "dislikes", "comment_count", "like_ratio", "comment_ratio"]
    categorical_columns = ["category_name", "channel_title_cleaned", "region",  "trending_day", "trending_month", "publish_day", "publish_hour"]
    yt_data_analysis = Analysis(path="./data/cleaned_data.csv", numerical_columns=numerical_columns, categorical_columns=categorical_columns)
    yt_data_analysis.get_data()
    # Univariate is only for testing how the data is behaving
    # Uncomment the next line to run univariate analysis(Note it will take time)
    # yt_data_analysis.univariate_analysis()
    yt_data_analysis.bivariate_analysis()
    yt_data_analysis.analyze_trends_over_time()
    
if __name__ == "__main__":
    main()   