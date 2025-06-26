# Day 75: Google Trends & Data Visualization

This project explores the relationship between Google search trends and real-world metrics such as stock prices, unemployment rates, and cryptocurrency values. Using Google Trends and various public data sources, it visualizes potential correlations and patterns over time.

---

## Project Features

* Visualization of **search interest vs. actual market data**
* Analysis of:

  * Tesla stock price vs. search volume
  * Bitcoin price vs. search volume
  * Unemployment rate vs. search interest for "Unemployment Benefits"
* Insights on how public interest may reflect or anticipate economic trends
* Time-series plotting and dual-axis charts

---

## Dataset Files

* `TESLA Search Trend vs Price.csv`
* `Bitcoin Search Trend.csv`
* `Daily Bitcoin Price.csv`
* `UE Benefits Search vs UE Rate 2004-19.csv`

---

## Technologies Used

* Python
* Pandas – for data wrangling
* Matplotlib – for data visualization
* Google Trends – source for search popularity data
* Yahoo Finance / FRED – financial and economic data

---

## How to Run

1. Clone the repository and go to the project directory:

   ```bash
   git clone https://github.com/thupham96/100-python-projects.git
   cd Day75_GoogleTrendsAnalysis
   ```

2. Install required libraries:

   ```bash
   pip install pandas matplotlib
   ```

3. Launch the notebook:

   ```bash
   jupyter notebook Google_Trends_and_Data_Visualisation.ipynb
   ```

---

## Key Insights

* Search popularity for Tesla and Bitcoin often spikes near major price events.
* Interest in "Unemployment Benefits" closely tracks U.S. unemployment trends.
* Google Trends can provide early signals of real-world changes in public behavior or economic conditions.

---

## What I Learned

* How to interpret and visualize Google Trends data
* Merging and aligning datasets with different time resolutions
* Dual-axis plots for comparing different data sources
* Exploring the relationship between public attention and financial indicators
