import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# 1. Load Data
df = pd.read_csv("housing.csv")

print("First 5 rows:\n", df.head())

# 2. Explore
print("\nMissing values:\n", df.isnull().sum())
print("\nStatistics:\n", df.describe())

# Correlation Heatmap
plt.figure(figsize=(8, 5))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# 3. Prepare Data
features = ["RM", "LSTAT", "PTRATIO", "INDUS", "NOX", "AGE"]
target = "MEDV"

X = df[features]
y = df[target]

# 4. Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 5. Model
model = LinearRegression()
model.fit(X_train, y_train)

# 6. Predict
y_pred = model.predict(X_test)

# 7. Evaluate
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print("MSE:", mse)
print("R2 Score:", r2)

# 8. Coefficients
coeff = pd.DataFrame(model.coef_, X.columns, columns=["Coefficient"])
print("\nFeature Importance:\n", coeff)

# 9. Plot
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Prices")
plt.ylabel("Predicted Prices")
plt.title("Actual vs Predicted Housing Prices")
plt.show()