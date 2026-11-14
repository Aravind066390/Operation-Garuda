# ==========================================
# AI Smart Grid - Load Prediction
# ==========================================

import pandas as pd
import numpy as np

from sklearn.preprocessing import MinMaxScaler

from tensorflow.keras.models import load_model

# ------------------------------------------
# Load Dataset
# ------------------------------------------

df = pd.read_csv("data/processed/clean_data.csv")

# ------------------------------------------
# Select Features
# ------------------------------------------

features = [
    "Hour",
    "Day",
    "Month",
    "Year",
    "Temperature",
    "Solar_Generation",
    "Wind_Generation",
    "EV_Demand"
]

X = df[features]

# ------------------------------------------
# Scale Data
# ------------------------------------------

scaler = MinMaxScaler()

X_scaled = scaler.fit_transform(X)

X_scaled = X_scaled.reshape((X_scaled.shape[0], X_scaled.shape[1], 1))

# ------------------------------------------
# Load Model
# ------------------------------------------

model = load_model("models/cnn_lstm_model.keras")

# ------------------------------------------
# Predict
# ------------------------------------------

predictions = model.predict(X_scaled)

df["Forecast_Load"] = predictions

# ------------------------------------------
# Display Results
# ------------------------------------------

print("\nFirst 10 Forecast Values\n")

print(df[["Datetime", "AEP_MW", "Forecast_Load"]].head(10))

# ------------------------------------------
# Save Results
# ------------------------------------------

df.to_csv("results/load_forecast.csv", index=False)

print("\nForecast Saved Successfully!")