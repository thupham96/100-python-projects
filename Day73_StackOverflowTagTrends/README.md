# Day 73: Stack Overflow Tag Trends Analysis

This project analyzes the popularity trends of various Stack Overflow programming tags over time. Using a dataset of monthly tag usage from 2008 to 2020, it visualizes how developer interest in languages and technologies has evolved.

---

## Project Features

* Time-series data analysis from **July 2008 to July 2020**
* Trends for **14 programming tags**, including:

  * `python`, `javascript`, `c#`, `java`, `php`, etc.
* Line charts showing tag usage over time
* Insights on technology growth and decline

---

## Technologies Used

* Python
* Pandas – data cleaning and analysis
* Matplotlib / Seaborn – data visualization
* Jupyter Notebook – for interactive exploration

---

## Dataset

CSV columns:

* `Date`: Monthly timestamp
* `Tag`: Programming tag name
* `PostCount`: Number of questions tagged

Example:

```
Date,Tag,PostCount
2008-07-01,c#,3
2008-08-01,python,124
...
```

---

## How to Run

1. Clone the repository and navigate to the project folder:

   ```bash
   git clone https://github.com/thupham96/100-python-projects.git
   cd Day73_StackOverflowTagTrends
   ```

2. Install dependencies:

   ```bash
   pip install pandas matplotlib seaborn
   ```

3. Launch the notebook:

   ```bash
   jupyter notebook StackOverflowTagTrends.ipynb
   ```

---

## Insights

* Python showed consistent growth, overtaking other languages.
* Legacy languages like `c` and `assembly` declined in relative popularity.
* Trends reflect industry shifts toward web, data science, and modern frameworks.

---

## What I Learned

* Time-series data cleaning and formatting in Pandas
* Plotting multiple trend lines for grouped data
* Real-world insights from Stack Overflow usage data
* Importance of visual storytelling in data analysis
