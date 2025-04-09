<div align="center">
  <h1><img src="your-project-logo.png" alt="Project Logo" width="150"> YouTube Channel Engagement Analysis 🎬📊</h1>
  <p>Uncovering the Secrets to Viral Success on YouTube</p>
</div>

---

## 🚀 Project Overview

This project dives deep into the "YouTube Trending Videos" dataset from Kaggle to understand the key factors that drive video popularity across different geographic regions and content categories. By leveraging the power of Python, Pandas, Seaborn, Matplotlib, and SQL, we aim to extract actionable insights into what makes a video go viral.

This repository contains the code and resources for the following stages of the analysis:

1.  **Data Cleaning with Pandas:** Ensuring data quality and consistency.
2.  **Exploratory Analysis with Seaborn/Matplotlib:** Visualizing trends, distributions, and relationships within the data.
3.  **SQL Queries for Aggregations and Joins:** Performing advanced data manipulation and extracting key metrics.
4.  **(Optional) Interactive Dashboard with Streamlit:** Creating a user-friendly interface to explore the findings.

## 🛠️ Technologies Used

* **Python:** The primary programming language for data manipulation and analysis.
* **Pandas:** For efficient data loading, cleaning, and manipulation.
* **Seaborn:** For creating informative and visually appealing statistical graphics.
* **Matplotlib:** For foundational plotting and customization.
* **SQLAlchemy:** For interacting with SQL databases (SQLite in this case).
* **(Optional) Streamlit:** For building and deploying the interactive dashboard.

## 📂 Repository Structure
├── data/                     # Contains the downloaded YouTube datasets (not committed due to size)
├── plots/                    # (Optional) Directory to store generated visualizations and results
├── data_cleaning.py          # Python script for data loading and cleaning
├── data_cleaning_initial.py  # Jupyter notebook to check how the data looks
├── analysis.py               # Data gathering/cleaning/concatinating/saving and Exploratory Data Analysis (EDA).
├── sql_analysis.py           # Python script for SQL queries and analysis
└── streamlit_dashboard.py    # (Optional) Python script for the Streamlit dashboard (COMING SOON)
├── README.md                 # The file you are currently reading
└── requirements.txt          # List of Python dependencies

## ⚙️ Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/agajankush/youtube-python-sql.git](https://github.com/agajankush/youtube-python-sql.git)
    cd youtube-python-sql
    ```

2.  **Install the required Python libraries:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Download the dataset:**
    * Go to the Kaggle link: [https://www.kaggle.com/datasets/datasnaek/youtube-new](https://www.kaggle.com/datasets/datasnaek/youtube-new)
    * Download the ZIP file and extract the `.csv` and `_category_id.json` files into the `data/` directory (you might need to create this directory).

## ▶️ Running the Code

1.  **Data Cleaning:**
    ```bash
    python data_cleaning.py
    ```
    This script will load the data, perform cleaning steps, merge category information, and save the cleaned data (e.g., `cleaned_data.csv`).

2.  **Exploratory Analysis:**
    ```bash
    python analysis.py
    ```
    This script will load the cleaned data and generate various visualizations to explore the data. The plots will be displayed on your screen.

3.  **SQL Analysis:**
    ```bash
    python sql_analysis.py
    ```
    This script will load the cleaned data into an SQLite database(in memory) and execute several SQL queries to perform aggregations and extract insights. The results will be printed to the console.

4.  **(COMING SOON) Streamlit Dashboard:**
    ```bash
    streamlit run streamlit_dashboard.py
    ```

## 📊 Key Findings (So Far)

* **Music Dominance:** The "Music" category consistently exhibits the highest average view counts across the majority of analyzed regions, suggesting a broad and highly engaged audience for music-related content.
* **Regional Engagement Preferences:** The United States and Great Britain tend to show higher overall average engagement (views, likes, and comments) compared to Canada.
* **Strong Positive Correlation:** A strong positive correlation exists between the number of views and the number of likes a video receives, indicating that higher viewership generally leads to more positive feedback.
* **Weekend Trending Peaks:** There is a noticeable increase in the number of new videos entering the trending charts on Fridays and Saturdays across several regions.
* **Top Channels:** Initial SQL analysis identifies "PewDiePie" and "T-Series" as consistently ranking among the channels with the highest total likes accumulated in the dataset.

## 💡 Future Enhancements

* Further in-depth analysis of temporal trends and seasonality.
* Sentiment analysis of video titles and descriptions.
* Building predictive models for video popularity.
* Expanding the Streamlit dashboard with more interactive features and visualizations.
* Exploring the impact of tags on video trending status.

## 🙌 Contributing

Contributions to this project are welcome! If you have ideas for improvements, new analyses, or bug fixes, please feel free to open an issue or submit a pull request.

## 📄 License

[Your License] (e.g., MIT License)

## 📧 Contact

[Ashutosh Gajankush] - [agajankush.github@gmail.com] - [https://www.linkedin.com/in/ashutoshgajankush/]

---

<div align="center">
  <p>Thank you for exploring this project! Feel free to connect and share your thoughts.</p>
</div>