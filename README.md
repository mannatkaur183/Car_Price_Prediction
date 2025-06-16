# Car Price Prediction using Gradient Boosting

This machine learning project focuses on predicting the **resale price of cars** using **Gradient Boosting**, a powerful ensemble learning technique. The model is trained on real car data and predicts the selling price based on key car features.

---

## Objective

- Predict the **selling price of used cars** based on factors like present price, kilometers driven, fuel type, etc.
- Use **Gradient Boosting Regressor** to achieve high prediction accuracy.

---

## 🛠 Technologies Used

- **Python**
- **Pandas** – for data manipulation
- **NumPy** – for numerical operations
- **Matplotlib & Seaborn** – for data visualization
- **Scikit-learn** – for model training and evaluation
  - `GradientBoostingRegressor`
  - `train_test_split`
  - `mean_absolute_error`, `r2_score`

---

##  Features Used

The model is trained on the following features:

- `Present_Price` – Ex-showroom price of the car
- `Kms_Driven` – Total distance driven
- `Owner` – Number of previous owners
- `Number_of_Years_Old` – Age of the car (calculated from manufacturing year)
- `Fuel_Type_Diesel`, `Fuel_Type_Petrol` – One-hot encoded fuel types
- `Seller_Type_Individual` – Whether the seller is an individual
- `Transmission_Manual` – Whether the car has a manual transmission

---

## ML Workflow

### 1. Data Preprocessing
- Dropped columns like `Car_Name`
- Performed one-hot encoding on categorical variables
- Engineered feature `Number_of_Years_Old` from the year

### 2. Model Training
- Model: `GradientBoostingRegressor`
- Data split: **80% training**, **20% testing**

### 3. Model Evaluation

| Metric                  | Value               |
|-------------------------|---------------------|
| **Accuracy**            | ✅ **93.01%**        |
| **Mean Absolute Error** | ✅ **0.7459 lakhs**  |

✔️ The model shows **excellent generalization** with low prediction error.

---

## 📊 Visualizations

- Correlation heatmaps for feature insights
- Pairplots for distribution and trends
- Count and bar plots for categorical analysis

---
![image](https://github.com/user-attachments/assets/495a8065-deab-44c6-9797-baa3a95ccaa9)

