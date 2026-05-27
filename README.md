# Predictive Maintenance Machine Learning Project

This project predicts machine failures using machine learning algorithms.

## Dataset
Predictive Maintenance Dataset from Kaggle:
https://www.kaggle.com/datasets/shivamb/machine-predictive-maintenance-classification

---

# Project Workflow

1. Data Loading
2. Exploratory Data Analysis (EDA)
3. Data Preprocessing
4. Train-Test Split
5. Model Training
6. Model Evaluation
7. Feature Importance Analysis

---

# Data Preprocessing

The following preprocessing steps were applied:

- Encoded categorical `Type` feature
- Removed unnecessary columns:
  - UDI
  - Product ID
  - Failure Type

---

# Machine Learning Models

The following models were used:

- Logistic Regression
- Decision Tree
- Random Forest

---

# Results

| Model | Accuracy |
|---|---|
| Logistic Regression | 0.974 |
| Decision Tree | 0.977 |
| Random Forest | 0.984 |

Random Forest produced the best overall performance.

---

# Feature Importance

Random Forest feature importance analysis showed that:

- Torque
- Rotational Speed
- Tool Wear

were the most influential features for predicting machine failures.

---

# Technologies Used

- Python
- Pandas
- Scikit-learn
- Matplotlib
- Jupyter Notebook

---

# How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the notebook:

```bash
jupyter notebook
```

Open:

```text
notebooks/analysis.ipynb
```
