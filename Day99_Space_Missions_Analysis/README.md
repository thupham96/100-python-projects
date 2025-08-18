# Day 99: Space Missions Analysis

This project explores the history of space missions from the dawn of the Space Race in 1957 to the modern era. Using data scraped from [nextspaceflight.com](https://nextspaceflight.com/launches/past/?page=1), it analyzes launch frequencies, countries’ contributions, and trends across decades of space exploration.

---

## Project Features

* **Data Exploration & Cleaning** — prepare mission data for analysis.
* **Country-Level Insights** — identify leading nations in space missions.
* **Temporal Trends** — visualize launches across decades.
* **Mission Outcomes** — analyze success vs. failure rates.
* **Interactive Visualizations** — explore launches with **Plotly** charts.

---

## Technologies Used

* **Python**
* **Pandas** — for data manipulation
* **NumPy** — numerical computing
* **Matplotlib & Seaborn** — for visualizations
* **Plotly Express** — for interactive charts
* **iso3166** — for country code lookups
* **Jupyter Notebook** — for analysis and reporting

---

## How to Run

1. Clone the repository and navigate to the project folder:

   ```bash
   git clone https://github.com/thupham96/100-python-projects.git
   cd Day99_Space_Missions_Analysis
   ```

2. Install dependencies:

   ```bash
   pip install pandas numpy matplotlib seaborn plotly iso3166
   ```

3. Open the notebook:

   ```bash
   jupyter notebook Space_Missions_Analysis.ipynb
   ```

---

## Key Insights

* Space exploration began with USA and USSR dominance, later joined by Europe, China, and private companies.
* Launches have accelerated in recent decades, reflecting commercial and scientific expansion.
* Success rates have improved significantly, but failures still occur in high-risk missions.
* Interactive charts reveal temporal and geographical shifts in global space activity.

---

## What I Learned

* Handling historical datasets with irregularities and missing values.
* Combining static (Seaborn/Matplotlib) and interactive (Plotly) visualizations.
* Analyzing categorical and temporal trends in large datasets.
* Applying storytelling techniques to data-driven exploration.
