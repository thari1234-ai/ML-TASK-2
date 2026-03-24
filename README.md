# 🏠 Housing Price Prediction using Multiple Linear Regression

## 📌 Project Overview

This project predicts the **median value of houses (MEDV)** based on various housing and neighborhood features using **Multiple Linear Regression**.

---

## 🎯 Objective

To analyze how different factors affect housing prices and build a predictive model.

---

## 📂 Project Structure

```
ML TASK-2/
│── housing.py
│── housing.csv
│── requirements.txt
│── README.md
```

---

## 📊 Dataset Description

| Feature | Description                 |
| ------- | --------------------------- |
| RM      | Average number of rooms     |
| LSTAT   | % lower status population   |
| PTRATIO | Pupil-teacher ratio         |
| INDUS   | Non-retail business area    |
| NOX     | Pollution level             |
| AGE     | Old housing proportion      |
| MEDV    | Median house value (target) |

---

## ⚙️ Technologies Used

* Python
* Pandas
* Scikit-learn
* Matplotlib
* Seaborn

---

## 🚀 Steps Performed

1. Data Loading
2. Data Exploration
3. Correlation Analysis (Heatmap)
4. Feature Selection
5. Model Training (Linear Regression)
6. Evaluation (MSE, R²)
7. Visualization

---

## 📈 Results

* Model predicts housing prices based on multiple features
* **MSE:** Varies
* **R² Score:** Close to 1 = better model

---

## 🔍 Key Insights

* 📈 **RM (rooms)** increases house price
* 📉 **LSTAT** decreases house price
* 📉 **PTRATIO** negatively affects price
* 📉 Pollution (NOX) reduces property value

---

## ▶️ How to Run

Install dependencies:

```
pip install pandas matplotlib seaborn scikit-learn
```

Run:

```
python housing.py
```

---

## ✅ Conclusion

Multiple Linear Regression effectively predicts housing prices and helps understand which features impact property value the most.

---

## 📌 Future Improvements

* Use full Boston dataset
* Feature scaling
* Try advanced models (Random Forest, XGBoost)

---

## 👨‍💻 Author

THARINI P 
E24AI049
