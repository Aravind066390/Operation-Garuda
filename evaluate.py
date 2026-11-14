# ==========================================
# AI Smart Grid - Model Evaluation
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np
import os

# Load prediction results
df = pd.read_csv("results/load_forecast.csv")

actual = df["AEP_MW"]
forecast = df["Forecast_Load"]

# Calculate metrics
mae = mean_absolute_error(actual, forecast)
rmse = np.sqrt(mean_squared_error(actual, forecast))
r2 = r2_score(actual, forecast)

print("=" * 50)
print("CNN-LSTM MODEL PERFORMANCE")
print("=" * 50)
print(f"MAE  : {mae:.2f}")
print(f"RMSE : {rmse:.2f}")
print(f"R²   : {r2:.4f}")

# Create results folder if needed
os.makedirs("results", exist_ok=True)

# Plot first 200 samples
plt.figure(figsize=(12,6))
plt.plot(actual[:200], label="Actual Load")
plt.plot(forecast[:200], label="Forecast Load")
plt.title("Actual vs Forecast Load")
plt.xlabel("Time")
plt.ylabel("Load (MW)")
plt.legend()

plt.savefig("results/forecast_graph.png", dpi=300)
plt.show()

print("\nGraph Saved Successfully!")