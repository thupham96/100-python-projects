# 📊 Day 72: College Major vs Salary Analysis

This project investigates how undergraduate majors impact salary outcomes across a career. Using a dataset with starting and mid-career salaries, we perform thorough analysis and visualizations to explore trends in salary growth, risk, and earning potential across fields like STEM, Business, and HASS.

---

## 📁 Files

* `salaries_by_college_major.csv` — Dataset with salary statistics per major.
* `salary_analysis.ipynb` — Notebook with step-by-step analysis and visualization.

---

## 💻 How to Run

```bash
git clone https://github.com/yourusername/100-python-projects.git
cd Day72_SalaryAnalysis
jupyter salary_analysis.ipynb
```

Or open it in **Google Colab**.

---

## 🧠 Key Analyses and Insights

### 🔍 1. Data Cleaning

* **Handled null values** and formatted salary columns by removing `$` and `,` for numerical processing.
* ✅ Result: Clean, numeric dataset ready for analysis.

---

### 📊 2. Salary Distributions (Histograms)

* **Starting Salary Distribution**: Most starting salaries cluster around **\$40,000–\$60,000**.
* **Mid-Career Salary Distribution**: Broader range, with many professionals earning between **\$70,000–\$110,000** by mid-career.

📌 *Insight: Salary potential increases significantly over time but with growing disparity.*

---

### 📈 3. Salary Growth (%) by Major

* Calculated **Growth %** = `(Mid-Career - Starting) / Starting * 100`.

🏆 **Top Growth Majors**:

| Major                   | Growth % |
| ----------------------- | -------- |
| Maths                   | 103.52   |
| Philosophy              | 103.51   |
| International Relations | 97.80    |

📌 *Insight: Majors like Philosophy and Math show high long-term growth despite modest starting pay.*

---

### 🎯 4. Salary Spread = Risk Level

* Defined **Risk** by the **spread between 90th and 10th percentile salaries**.
* Flagged majors as `High` or `Low` risk based on the median spread.

🔥 **High Risk (Wide Spread)**:

* Economics
* Finance
* Maths

📌 *Insight: Humanities majors often have wide income variability—higher potential upside but also downside.*

---

### 🥇 5. Highest & Lowest Salary Percentiles

* **Top 90th Percentile (High Reward)**:

  * Economics: \$210K
  * Finance: \$195K
  * Chemical Engineering: \$194K

* **Bottom 10th Percentile (Low Floor)**:

  * Music, Art History, and Education: \~\$25K–\$30K

📌 *Insight: STEM majors dominate the high end; education and social sciences appear more stable but lower earning.*

---

### 🪜 6. Mid-Career Median Salary (Bar Chart)

![Bar chart showing top 10 mid-career salaries](#)

🤑 **Top Earners by Mid-Career Median**:

* Chemical Engineering
* Computer Engineering
* Electrical Engineering

📌 *Insight: Engineering consistently ranks at the top across all salary metrics.*

---

### 📉 7. Starting vs Mid-Career Salary (Scatter Plot)

* **Positive correlation** between starting salary and mid-career earnings.
* Some outliers with low starting but high long-term payoff (e.g., Philosophy).

📌 *Insight: A high starting salary often predicts higher lifetime income, but not always.*

---

### 📦 8. Salary by Group (Box Plot)

* Compared STEM, Business, and HASS majors.
* **STEM**: Highest median and narrowest interquartile range.
* **HASS**: Wider spread, lower medians.

📌 *Insight: STEM provides consistent high-paying outcomes, while HASS is more variable.*

---

## 📚 Learning Outcomes

* 🧹 Data cleaning and preparation with Pandas.
* 📊 Exploratory Data Analysis (EDA) techniques.
* 📈 Visual storytelling using Matplotlib & Seaborn.
* 🎓 Domain insight into education and labor market trends.

---

## 🧰 Technologies Used

* Python 3.x
* Jupyter Notebook
* Pandas
* Matplotlib & Seaborn
