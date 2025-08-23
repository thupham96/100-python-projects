# Day 100: Fatal Force – Police Shootings Analysis in the U.S.

This project analyzes fatal police shootings in the United States from **2015 onward**, using data compiled by *The Washington Post*. The dataset includes demographics (age, race, gender), mental illness indicators, and situational details of each fatal encounter, along with socioeconomic data from the U.S. Census (poverty rate, income, education, racial composition).

The project aims to uncover **patterns, disparities, and geographic trends** in police killings, highlighting systemic issues and correlations with broader social factors.

---

## Project Features

* **Data Exploration & Cleaning** — checked for missing values, duplicates, and standardized data across five datasets.
* **Demographic Analysis** — studied distribution of victims by age, race, and gender.
* **Mental Health Impact** — assessed frequency of victims with reported mental illness.
* **Geographic Insights** — visualized top cities and states with highest fatalities, including choropleth maps.
* **Socioeconomic Correlation** — compared police killings with poverty, education, and income by state.
* **Temporal Trends** — explored killings over time to identify spikes or long-term patterns.
* **Interactive Visualizations** — created with **Plotly** for deep exploration.

---

## Technologies Used

* **Python**
* **Pandas & NumPy** — data wrangling and preprocessing
* **Matplotlib & Seaborn** — static visualizations
* **Plotly Express** — interactive charts & choropleths
* **Jupyter Notebook** — analysis and reporting environment

---

## How to Run

1. Clone the repository and navigate to the project folder:

   ```bash
   git clone https://github.com/thupham96/100-python-projects.git
   cd Day100_Fatal_Force_Analysis
   ```

2. Install dependencies:

   ```bash
   pip install pandas numpy matplotlib seaborn plotly
   ```

3. Open the notebook:

   ```bash
   jupyter notebook Fatal_Force.ipynb
   ```

---

## Key Insights

* **Victim Demographics**

  * Majority are young to middle-aged adults (20s–30s).
  * Black and Native American individuals are disproportionately represented relative to their share of the U.S. population.
  * Around **25% of victims** show signs of mental illness — far above the national prevalence rate (\~5–6%).

* **Geographic Trends**

  * **Los Angeles, Phoenix, Houston, and Chicago** top the list of cities with the most killings.
  * Large states like **California, Texas, and Florida** account for the highest totals.
  * Southern states with **higher poverty rates** also report elevated incidents.

* **Socioeconomic Links**

  * States with **high poverty and low education rates** tend to have more police killings.
  * The overlap suggests systemic socioeconomic factors influence fatal encounters.

* **Temporal Patterns**

  * Fatal police shootings remain consistently high year to year since 2015, with no strong downward trend.

---

## What I Learned

* Cleaning and joining multiple datasets with different encodings and structures.
* Using both static (Matplotlib/Seaborn) and interactive (Plotly) visualizations for storytelling.
* Analyzing demographic and socioeconomic disparities with real-world implications.
* Interpreting data with sensitivity, considering **context, systemic bias, and limitations** of reporting.

---

🎉 **Day 100 marks the completion of the 100 Python Projects challenge!**
This final project reflects the integration of **data wrangling, visualization, and storytelling** to highlight important societal issues through code.
