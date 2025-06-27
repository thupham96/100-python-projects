# Day 76: Google Play Store App Analytics

This project analyzes the Android app market by exploring a dataset of thousands of apps from the Google Play Store. It focuses on cleaning, processing, and visualizing app data to uncover trends in ratings, categories, pricing, and popularity.

---

## Project Features

* Cleaning and preprocessing app data:

  * Removing unused columns
  * Handling NaN values
  * Stripping symbols from price and install counts
  * Removing duplicates
* Analysis of:

  * App categories and average ratings
  * Distribution of app prices and types (free vs paid)
  * Popularity based on installs
* Visualizations using Matplotlib, Seaborn, and Plotly

---

## Dataset

* `apps.csv` — includes details such as:

  * `App`
  * `Category`
  * `Rating`
  * `Reviews`
  * `Size`
  * `Installs`
  * `Price`
  * `Type`
  * `Content Rating`
  * `Genres`
  * `Last Updated`
  * `Current Ver`
  * `Android Ver`

---

## Technologies Used

* Python
* Pandas – for data cleaning and analysis
* Matplotlib & Seaborn – for static visualizations
* Plotly – for interactive charts
* Jupyter Notebook – for exploration

---

## How to Run

1. Clone the repo and navigate to the project directory:

   ```bash
   git clone https://github.com/thupham96/100-python-projects.git
   cd Day76_GooglePlayAppAnalytics
   ```

2. Install dependencies:

   ```bash
   pip install pandas matplotlib seaborn plotly
   ```

3. Open the notebook:

   ```bash
   jupyter notebook Google_Play_Store_App_Analytics.ipynb
   ```

---

## Key Insights

* Free apps dominate the store, but paid apps tend to have slightly higher average ratings.
* Most apps cluster around the low install ranges, with a few outliers having billions of installs.
* The most common app categories include `FAMILY`, `GAME`, and `TOOLS`.

---

## What I Learned

* Cleaning messy datasets with missing values, duplicates, and unwanted characters
* Using Pandas for grouping and aggregating data
* Creating both static and interactive visualizations
* Interpreting app market trends through data
