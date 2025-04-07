import pandas as pd

def data_cleaning():
    data = pd.read_csv("./data/USvideos.csv")
    aggerate = data.groupby("title")["views"].sum()
    sorted_agg = aggerate.sort_values(ascending=False)
    merged_agg = data.merge(sorted_agg, on="title", how="left").sort_values(["views_y"], ascending=False)
    merged_agg.loc[:, ["title", "category_id", "views_x", "views_y"]].head(10)
    copy_merged = merged_agg.copy()
    copy_merged.drop_duplicates(subset=["title"], inplace=True)
    copy_merged.sort_values(["views_y"], ascending=False).head(10)
    top_10_videos = copy_merged.loc[:, ["title", "category_id", "views_x", "views_y"]].head(10)
    top_10_videos["region"] = "US"
    category_data_raw = pd.read_json("./data/US_category_id.json")
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
    return final_data





