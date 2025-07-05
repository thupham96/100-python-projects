# Day 81: 🏠 Multivariable Regression and Valuation Model

This project builds a multivariable linear regression model to estimate residential property values in Boston using 1970s housing data. It demonstrates how statistical modeling and data transformation can help predict house prices based on characteristics like number of rooms, distance to employment centers, and socioeconomic factors.

---

## Project Features

* Loading and exploring the Boston Housing dataset
* Visualizing relationships between predictors and house prices
* Building a **multivariable linear regression model**
* Interpreting model coefficients to understand feature importance
* Evaluating model performance and analyzing residuals
* Applying data transformations (e.g., log price) to improve model fit
* Making predictions for house valuations

---

## Technologies Used

* **Python**
* **Pandas** — for data manipulation
* **NumPy** — for numerical operations
* **Matplotlib** & **Seaborn** — for data visualization
* **Plotly** — for interactive charts
* **Scikit-learn** — for linear regression modeling

---

## How to Run

1. Clone the repository and navigate to the project directory:

   ```bash
   git clone https://github.com/thupham96/100-python-projects.git
   cd Day81_Multivariable_Regression
   ```

2. Install the required dependencies:

   ```bash
   pip install pandas numpy matplotlib seaborn plotly scikit-learn
   ```

3. Open the notebook:

   ```bash
   jupyter notebook Multivariable_Regression_and_Valuation_Model.ipynb
   ```

---

## Key Insights

* **Number of rooms (RM)** shows a positive relationship with house price.
* **LSTAT (lower status population percentage)** is negatively associated with price, indicating socioeconomic factors significantly impact valuation.
* **Distance to employment centers (DIS)** and proximity to industrial zones (INDUS) also play notable roles in predicting price.
* Applying a log transformation to the target (price) can improve model linearity and interpretability.

---

## What I Learned

* Building and interpreting multivariable regression models
* The impact of feature scaling and transformation on regression performance
* Techniques for evaluating residuals and model goodness-of-fit
* The importance of data storytelling when presenting valuation models
