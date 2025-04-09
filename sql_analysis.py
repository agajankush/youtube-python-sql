import pandas as pd
from sqlalchemy import create_engine
from pydantic import BaseModel

engine = create_engine('sqlite:///:memory:')
class SQLQuery(BaseModel):
    path: str
    query: str = None
    df_cleaned: pd.DataFrame = None
    engine: object = None
    
    class Config:
        arbitrary_types_allowed = True
    

    def load_data(self):
        self.engine = create_engine('sqlite:///:memory:')
        self.df_cleaned = pd.read_csv(self.path)
        # Load DataFrame into SQL Database
        self.df_cleaned.to_sql('cleaned_data', self.engine, index=False, if_exists='replace')
        print("Data loaded into SQL database successfully.")
    
    def execute_query(self):
        if self.engine is None:
            self.load_data()
        # Average views by category name
        query_avg_views_category = """
            SELECT category_name, AVG(views) AS average_views
            FROM cleaned_data
            GROUP BY category_name
            ORDER BY average_views DESC;
        """
        avg_views_category = pd.read_sql_query(query_avg_views_category, self.engine)
        print("\nAverage Views by Category:")
        print(avg_views_category)
        
        # Total liked by cleaning channel title
        query_total_likes_channel = """
            SELECT channel_title, SUM(likes) AS total_likes
            FROM cleaned_data
            GROUP BY channel_title
            ORDER BY total_likes DESC
            LIMIT 10;
        """
        total_likes_channel = pd.read_sql_query(query_total_likes_channel, self.engine)
        print("\nTotal Likes by Channel Title:")
        print(total_likes_channel)
        
        # Videos with more than 1 million views in the US
        high_views_in_us = """
            SELECT title_cleaned, views
            FROM cleaned_data
            WHERE views > 1000000 AND region = 'US'
            ORDER BY views DESC
            LIMIT 10;
        """
        high_views_us = pd.read_sql_query(high_views_in_us, self.engine)
        print("\nVideos with more than 1 million views in the US:")
        print(high_views_us)
        
        # Average like ratio by category name
        avg_like_ratio_category = """
            SELECT category_name, AVG(like_ratio) AS average_like_ratio
            FROM cleaned_data
            GROUP BY category_name
            ORDER BY average_like_ratio DESC;
        """
        avg_like_ratio = pd.read_sql_query(avg_like_ratio_category, self.engine)
        print("\nAverage Like Ratio by Category:")
        print(avg_like_ratio)
        
        # Most Frequent trending day by region
        trending_day_region = """
            SELECT region, trending_day, COUNT(*) AS count
            FROM cleaned_data
            GROUP BY region, trending_day
            ORDER BY count DESC;
        """
        trending_day = pd.read_sql_query(trending_day_region, self.engine)
        print("\nMost Frequent Trending Day by Region:")
        print(trending_day)

def main():
    sql_analysis = SQLQuery(path="./data/cleaned_data.csv")
    sql_analysis.execute_query()
    
if __name__ == "__main__":
    main()
