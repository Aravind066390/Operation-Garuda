# ==========================================
# AI Smart Grid - CNN-LSTM Load Forecasting
# ==========================================

import pandas as pd
import numpy as np
import os

from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv1D, LSTM, Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping

# ------------------------------------------
# Load Dataset
# ------------------------------------------

df = pd.read_csv("data/processed/clean_data.csv")

print("Dataset Loaded Successfully!")

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

target = "AEP_MW"

X = df[features]

y = df[target]

# ------------------------------------------
# Feature Scaling
# ------------------------------------------

scaler = MinMaxScaler()

X_scaled = scaler.fit_transform(X)

# ------------------------------------------
# Reshape for CNN-LSTM
# ------------------------------------------

X_scaled = X_scaled.reshape((X_scaled.shape[0], X_scaled.shape[1], 1))

# ------------------------------------------
# Train/Test Split
# ------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X_scaled,
    y,
    test_size=0.2,
    random_state=42
)

# ------------------------------------------
# Build CNN-LSTM Model
# ------------------------------------------

model = Sequential()

model.add(
    Conv1D(
        filters=64,
        kernel_size=2,
        activation="relu",
        input_shape=(X_train.shape[1], 1)
    )
)

model.add(Dropout(0.2))

model.add(
    LSTM(64)
)

model.add(Dense(32, activation="relu"))

model.add(Dense(1))

model.compile(
    optimizer="adam",
    loss="mse",
    metrics=["mae"]
)

model.summary()

# ------------------------------------------
# Train Model
# ------------------------------------------

early_stop = EarlyStopping(
    patience=5,
    restore_best_weights=True
)

history = model.fit(
    X_train,
    y_train,
    validation_split=0.2,
    epochs=20,
    batch_size=64,
    callbacks=[early_stop],
    verbose=1
)

# ------------------------------------------
# Save Model
# ------------------------------------------

os.makedirs("models", exist_ok=True)

model.save("models/cnn_lstm_model.keras")

print("\nCNN-LSTM Model Saved Successfully!")