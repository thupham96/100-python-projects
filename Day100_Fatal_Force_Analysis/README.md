# Day 100: **Fatal Force — U.S. Police Killings Analysis (2015–Present)**

This capstone project analyzes U.S. police killings using the Washington Post **Fatal Force** dataset. The notebook explores trends over time, geography (state & city), demographics, and incident characteristics such as threat level, fleeing status, and body-camera usage.

---

## Project Features

* **Data Cleaning & Standardization**

  * Normalize city names (e.g., removing “city/town/cdp”, trimming spaces) and map race codes.
  * Handle missing/unknown values and ensure consistent types for time-series analysis.
* **Temporal Trends**

  * Annual and monthly incident counts; rolling averages for smoother trends.
* **Geographic Patterns**

  * Top states and cities by incident counts; choropleth by state.
* **Incident Characteristics**

  * Distributions by `manner_of_death`, `armed`, `threat_level`, `flee`, `signs_of_mental_illness`, `body_camera`.
* **Interactive Visualizations**

  * Plotly charts with hover tooltips and filters for exploratory analysis.

---

## Data Sources

* **The Washington Post — Fatal Force** (police shootings database, 2015–present)
  Typical columns used: `date`, `state`, `city`, `age`, `gender`, `race`, `manner_of_death`, `armed`, `threat_level`, `flee`, `signs_of_mental_illness`, `body_camera`.

> ⚠️ Ethics & Limitations: These data represent deaths, not all police–civilian encounters. Reporting practices, definitions, and missingness can bias results. Treat insights as descriptive, not causal.

---

## Technologies Used

* **Python**, **Pandas**, **NumPy**
* **Matplotlib & Seaborn** for static plots
* **Plotly Express** for interactive charts
* **Jupyter Notebook**
* *(Optional)* **iso3166** for country/state code utilities (if needed)

---

## How to Run

1. **Clone & Enter Folder**

   ```bash
   git clone https://github.com/thupham96/100-python-projects.git
   cd Day100_Fatal_Force_Analysis
   ```

2. **Install Dependencies**

   ```bash
   pip install pandas numpy matplotlib seaborn plotly iso3166
   ```

3. **Add Data**

   * Place the Fatal Force CSV in `data/fatal-police-shootings-data.csv`.
   * (Optional) Place FiveThirtyEight’s file in `data/share_race_city.csv`.

4. **Open the Notebook**

   ```bash
   jupyter notebook Fatal_Force_Analysis.ipynb
   ```

---

## Key Visuals & Analyses

* **Incidents Over Time**: yearly & monthly trends with rolling averages.
* **By State**: bar chart of counts; Plotly choropleth map.
* **Top Cities**: top-N cities after name standardization (see “City Cleaning” below).
* **Demographics**: stacked bars of incidents by race & gender (with “Unknown” shown).
* **Incident Details**: distributions for `armed`, `threat_level`, `flee`, `signs_of_mental_illness`, and `body_camera`.

---

## City Cleaning & Share Re-Normalization (Tip)

When consolidating city names (e.g., “Chicago city”, “Chicago town”, “Chicago CDP” → “chicago”), demographic **shares** from `share_race_city` can sum to more than 100% if you simply merge rows. Re-normalize after grouping:

```python
# Standardize city names in both dataframes
def clean_city(s):
    return (s.str.lower()
             .str.replace(r'\s*(city|town|cdp)\b', '', regex=True)
             .str.replace(' ', '', regex=False))

df_fatal['cleaned_city'] = clean_city(df_fatal['city'])
df_share['cleaned_city'] = clean_city(df_share['City'])

# Aggregate share rows by cleaned city and state, then renormalize to 1.0
share_cols = [
    'share_white','share_black','share_hispanic',
    'share_asian','share_native_american','share_other'
]

agg = (df_share
       .groupby(['state', 'cleaned_city'], as_index=False)[share_cols]
       .mean())

agg[share_cols] = agg[share_cols].div(agg[share_cols].sum(axis=1), axis=0)
```

This ensures each city’s demographic shares still total 100% after consolidation.

---

## What I Learned

* Robust **data cleaning** across heterogeneous sources (e.g., reconciling city labels).
* Managing **categorical & temporal** analyses with missing/unknown values.
* Designing **honest visualizations** (showing “Unknown” explicitly, adding uncertainty notes).
* Building **interactive EDA** workflows with Plotly for deeper, faster exploration.
* Communicating **limitations & ethics** clearly in a sensitive analytical domain.

---

## Next Steps

* Expand geography to **county/metro** rollups and normalize by population rates.
* Add **significance tests** or **Bayesian models** for over/under-representation.
* Incorporate **policy/context features** (e.g., state laws, body-cam mandates) for richer analysis.
* Build a small **Dash** app to let users filter by state, city, and year interactively.

---

## Acknowledgments

* Data journalism by **The Washington Post** (Fatal Force).
* Thanks to the broader open-data community for maintaining and discussing these datasets.

---

*Milestone unlocked: Day 100! 🎉 Thanks for following along this 100-day journey.*
