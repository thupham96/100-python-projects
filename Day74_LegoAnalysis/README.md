# Day 74: LEGO Data Analysis

This project explores LEGO set data across themes, colors, and years using Python and Pandas. It analyzes the evolution of LEGO sets, the most popular themes, the variety of colors used, and trends in set releases over time.

---

## Project Features

* Analysis of LEGO sets from early years to recent times
* Breakdown of **most common themes**
* Exploration of **color usage** (transparent vs opaque)
* Time-series visualization of **sets released per year**
* Merging data across multiple datasets (`sets.csv`, `themes.csv`, `colors.csv`)

---

## Dataset Files

* `sets.csv` – Details of LEGO sets, including year, theme, and set name
* `themes.csv` – Mapping of theme ID to theme name
* `colors.csv` – List of LEGO brick colors and transparency information

---

## Technologies Used

* Python
* Pandas – for data manipulation and merging
* Matplotlib – for plotting trends
* Jupyter Notebook – for interactive analysis

---

## How to Run

1. Clone the repository and go to the project folder:

   ```bash
   git clone https://github.com/thupham96/100-python-projects.git
   cd Day74_LegoAnalysis
   ```

2. Install dependencies:

   ```bash
   pip install pandas matplotlib
   ```

3. Open the Jupyter notebook:

   ```bash
   jupyter notebook Lego_Analysis.ipynb
   ```

---

## Key Insights

* LEGO set production significantly increased post-2000.
* Some themes like `Star Wars`, `City`, and `Technic` dominate the set count.
* A wide variety of brick colors are used, with a mix of transparent and opaque types.

---

## What I Learned

* How to clean and merge real-world datasets
* Analyzing and grouping data by categories (e.g. theme, year)
* Visualizing insights with bar plots and time series
* Exploring relationships between sets, themes, and colors
