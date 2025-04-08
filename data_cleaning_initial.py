import pandas as pd

def data_cleaning(country):
    data = None
    try:
        data = pd.read_csv(f"./data/{country}videos.csv")
    except:
        data = pd.read_csv(f"./data/{country}videos.csv", encoding="utf-8")
        
    aggerate = data.groupby("title")["views"].sum()
    sorted_agg = aggerate.sort_values(ascending=False)
    merged_agg = data.merge(sorted_agg, on="title", how="left").sort_values(["views_y"], ascending=False)
    copy_merged = merged_agg.copy()
    copy_merged.drop_duplicates(subset=["title"], inplace=True)
    copy_merged.sort_values(["views_y"], ascending=False).head(10)
    top_10_videos = copy_merged.loc[:, ["title", "category_id", "views_x", "views_y"]].head(20)
    top_10_videos["region"] = country
    category_data_raw = pd.read_json(f"./data/{country}_category_id.json")
    category_data = category_data_raw["items"].apply(pd.Series)
    def get_category_name(item):
        return item["snippet"]["title"]
    category_data["category_name"] = category_data.apply(get_category_name, axis=1)
    category_data["id"] = pd.to_numeric(category_data["id"])
    final_data = pd.merge(
        top_10_videos,
        category_data,
        left_on="category_id",
        right_on="id",
        how="left",
    )
    return final_data[["title", "views_y", "region", "category_name"]]


def main():
    countries = ["CA", "GB", "DE", "FR", "IN", "US", "RU", "MX", "JP", "KR"]
    for country in countries:
        print(f"Processing {country}...")
        cleaned_data = data_cleaning(country)
        print(cleaned_data)

if __name__ == "__main__":
    main()

