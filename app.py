import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

from tensorflow.keras.models import load_model


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="AI Smart Grid Dashboard",
    page_icon="⚡",
    layout="wide"
)


# ============================================================
# LOAD DATA
# ============================================================

@st.cache_data
def load_data():
    data = pd.read_csv("results/load_forecast.csv")
    data["Datetime"] = pd.to_datetime(data["Datetime"])
    data = data.sort_values("Datetime")
    return data


df = load_data()


# ============================================================
# LOAD DQN MODEL
# ============================================================

@st.cache_resource
def load_dqn_model():
    return load_model(
        "models/dqn_energy_management.keras",
        compile=False
    )


dqn_model = load_dqn_model()


# ============================================================
# TITLE
# ============================================================

st.title(
    "⚡ AI-Powered Intelligent Load Forecasting "
    "and Energy Management System"
)

st.markdown("### Smart Distribution Networks")

st.markdown("---")

st.write("### WattNext26 Project Competition")
st.write(
    "Department of Electrical and Electronics Engineering"
)
st.write(
    "University College of Engineering Kanchipuram"
)


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("Navigation")

st.sidebar.success("WattNext26 Project")

st.sidebar.markdown("---")

st.sidebar.write("✅ Federated Learning")
st.sidebar.write("✅ CNN-LSTM Load Forecasting")
st.sidebar.write("✅ Deep Reinforcement Learning")
st.sidebar.write("✅ Explainable AI")
st.sidebar.write("✅ Energy Management")
st.sidebar.write("✅ Transformer Monitoring")


# ============================================================
# KPI VALUES
# ============================================================

current_load = float(df["AEP_MW"].iloc[-1])

forecast_average = float(
    df["Forecast_Load"].mean()
)

peak_load = float(
    df["Forecast_Load"].max()
)


# ============================================================
# KPI CARDS
# ============================================================

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Current Load",
    f"{current_load:,.2f} MW"
)

col2.metric(
    "Average Forecast Load",
    f"{forecast_average:,.2f} MW"
)

col3.metric(
    "Peak Forecast Load",
    f"{peak_load:,.2f} MW"
)

col4.metric(
    "Grid Status",
    "Normal ✅"
)


st.markdown("---")


# ============================================================
# WELCOME
# ============================================================

st.header("Welcome")

st.write(
    """
This dashboard demonstrates:

- 🌐 Federated Learning
- 📈 CNN-LSTM Load Forecasting
- 🧠 Deep Reinforcement Learning
- 💡 Explainable AI
- 🔋 Battery Energy Management
- 🚗 EV Charging Optimization
- ☀️ Renewable Energy Management
- 🚨 Transformer Overload Monitoring
"""
)


st.markdown("---")


# ============================================================
# AI LOAD FORECASTING
# ============================================================

st.header("📈 AI Load Forecasting")

st.write(
    "Actual Load vs Forecasted Load using CNN-LSTM Model"
)

forecast_graph_data = df.head(300)

fig = px.line(
    forecast_graph_data,
    x="Datetime",
    y=[
        "AEP_MW",
        "Forecast_Load"
    ],
    labels={
        "value": "Load (MW)",
        "Datetime": "Time",
        "variable": "Load Type"
    },
    title="Actual Load vs Forecast Load"
)

st.plotly_chart(
    fig,
    use_container_width=True
)


st.subheader("Model Performance")

col1, col2 = st.columns(2)

col1.metric(
    "Forecasting Model",
    "CNN-LSTM"
)

col2.metric(
    "R² Score",
    "0.6282"
)


st.markdown("---")


# ============================================================
# FEDERATED LEARNING
# ============================================================

st.header("🌐 Federated Learning")

st.write(
    "Privacy-Preserving Distributed AI Training"
)

col1, col2, col3, col4 = st.columns(4)

col1.success(
    "🟢 Smart Meter A\n\nConnected"
)

col2.success(
    "🟢 Smart Meter B\n\nConnected"
)

col3.success(
    "🟢 Smart Meter C\n\nConnected"
)

col4.info(
    "🖥️ Central Server\n\nActive"
)


with st.container(border=True):

    st.subheader(
        "Federated Learning Workflow"
    )

    st.markdown(
        """
- Smart Meter A trains its local AI model.
- Smart Meter B trains its local AI model.
- Smart Meter C trains its local AI model.
- Only model updates are sent to the Central Server.
- Raw consumer data never leaves the smart meters.
- The server aggregates local updates into a global model.
"""
    )


st.markdown("---")


# ============================================================
# REAL-TIME SMART GRID SIMULATION
# ============================================================

st.header(
    "⚡ Real-Time Smart Grid Simulation"
)

st.write(
    "Change the simulation hour to monitor AI forecast "
    "and DRL grid operation."
)


simulation_hour = st.slider(
    "Select Simulation Hour",
    min_value=0,
    max_value=23,
    value=12,
    step=1
)


hour_data = df[
    df["Datetime"].dt.hour == simulation_hour
]


if hour_data.empty:

    st.error(
        "No simulation data available."
    )

    st.stop()


simulation_row = hour_data.iloc[-1]


simulation_actual = float(
    simulation_row["AEP_MW"]
)

simulation_forecast = float(
    simulation_row["Forecast_Load"]
)


st.subheader("Live Grid Parameters")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Simulation Time",
    f"{simulation_hour:02d}:00"
)

col2.metric(
    "Actual Load",
    f"{simulation_actual:,.2f} MW"
)

col3.metric(
    "AI Forecast Load",
    f"{simulation_forecast:,.2f} MW"
)


# ============================================================
# DYNAMIC SIMULATION GRAPH
# ============================================================

st.subheader(
    "📊 Hour-Based Load Analysis"
)

simulation_graph_data = hour_data.tail(100)

simulation_fig = px.line(
    simulation_graph_data,
    x="Datetime",
    y=[
        "AEP_MW",
        "Forecast_Load"
    ],
    labels={
        "value": "Load (MW)",
        "Datetime": "Datetime",
        "variable": "Load Type"
    },
    title=(
        f"Load Analysis for Hour "
        f"{simulation_hour:02d}:00"
    )
)

st.plotly_chart(
    simulation_fig,
    use_container_width=True
)


st.markdown("---")


# ============================================================
# DEEP REINFORCEMENT LEARNING DECISION LAYER
# ============================================================

st.header("🧠 AI Decision Layer")

st.write(
    "Deep Reinforcement Learning Based Energy Management"
)


# ============================================================
# CREATE 5-FEATURE DRL STATE
# ============================================================

drl_state = np.array(
    [[
        simulation_forecast / 20000.0,
        float(simulation_row["Hour"]) / 23.0,
        float(
            simulation_row["Solar_Generation"]
        ) / 500.0,
        float(
            simulation_row["Wind_Generation"]
        ) / 500.0,
        float(
            simulation_row["EV_Demand"]
        ) / 200.0
    ]],
    dtype=np.float32
)


# ============================================================
# DQN PREDICTION
# ============================================================

q_values = dqn_model.predict(
    drl_state,
    verbose=0
)

action = int(
    np.argmax(q_values[0])
)


# ============================================================
# DEBUG / DRL EXPLAINABILITY
# ============================================================

with st.expander(
    "🔍 View DRL Model Output"
):

    st.write(
        "DRL State:",
        drl_state
    )

    st.write(
        "DQN Q-Values:",
        q_values
    )

    st.write(
        "Selected Action:",
        action
    )


# ============================================================
# ACTION MAPPING
# ============================================================

action_names = {
    0: "Normal Operation",
    1: "Battery Discharge",
    2: "Delay EV Charging",
    3: "Use Renewable Energy"
}


selected_action = action_names[action]


battery_decision = "Standby"
ev_decision = "Normal Charging"
renewable_decision = "Normal Utilization"


if action == 0:

    battery_decision = "Standby"

    ev_decision = "Normal Charging"

    renewable_decision = "Normal Utilization"


elif action == 1:

    battery_decision = "Discharge"

    ev_decision = "Normal Charging"

    renewable_decision = "Normal Utilization"


elif action == 2:

    battery_decision = "Standby"

    ev_decision = "Delayed"

    renewable_decision = "Normal Utilization"


elif action == 3:

    battery_decision = "Standby"

    ev_decision = "Normal Charging"

    renewable_decision = "Increase Solar + Wind"


# ============================================================
# ENERGY MANAGEMENT CARDS
# ============================================================

col1, col2, col3 = st.columns(3)

col1.success(
    f"🔋 Battery\n\n{battery_decision}"
)

col2.warning(
    f"🚗 EV Charging\n\n{ev_decision}"
)

col3.info(
    f"☀️ Renewable Energy\n\n{renewable_decision}"
)


# ============================================================
# DRL RECOMMENDATION
# ============================================================

st.subheader("DRL Recommendation")

st.info(
    f"""
Forecast Load : **{simulation_forecast:,.2f} MW**

DRL Selected Action : **{selected_action}**

Battery Control : **{battery_decision}**

EV Charging : **{ev_decision}**

Renewable Energy : **{renewable_decision}**
"""
)


st.markdown("---")


# ============================================================
# EXPLAINABLE AI
# ============================================================

st.header("💡 Explainable AI")

st.write(
    "Feature Importance Generated from "
    "the Explainability Model"
)

st.image(
    "results/feature_importance.png",
    caption="AI Feature Importance",
    use_container_width=True
)


# ============================================================
# CALCULATED CONFIDENCE SCORE
# ============================================================

prediction_error = abs(
    simulation_actual - simulation_forecast
)

if simulation_actual != 0:

    confidence_score = (
        1 - (
            prediction_error /
            abs(simulation_actual)
        )
    ) * 100

else:

    confidence_score = 0


confidence_score = max(
    0,
    min(
        100,
        confidence_score
    )
)


st.subheader(
    "🎯 AI Forecast Confidence Score"
)

col1, col2, col3 = st.columns(3)

col1.metric(
    "Actual Load",
    f"{simulation_actual:,.2f} MW"
)

col2.metric(
    "Forecast Load",
    f"{simulation_forecast:,.2f} MW"
)

col3.metric(
    "Confidence Score",
    f"{confidence_score:.2f}%"
)


if confidence_score >= 90:

    st.success(
        "🟢 High Confidence Prediction"
    )

elif confidence_score >= 75:

    st.warning(
        "🟡 Moderate Confidence Prediction"
    )

else:

    st.error(
        "🔴 Low Confidence Prediction"
    )


st.markdown("---")


# ============================================================
# TRANSFORMER MONITORING
# ============================================================

st.header(
    "🚨 Transformer Overload Monitoring"
)

st.write(
    "AI-Based Transformer Load Monitoring"
)


transformer_capacity = 20000.0

loading_percentage = (
    simulation_forecast /
    transformer_capacity
) * 100


col1, col2, col3 = st.columns(3)

col1.metric(
    "Forecast Load",
    f"{simulation_forecast:,.2f} MW"
)

col2.metric(
    "Transformer Capacity",
    f"{transformer_capacity:,.0f} MW"
)

col3.metric(
    "Transformer Loading",
    f"{loading_percentage:.2f}%"
)


st.progress(
    min(
        1.0,
        loading_percentage / 100
    )
)


if loading_percentage >= 85:

    st.error(
        "🚨 Transformer Overload Alert! "
        "Immediate Energy Management Required."
    )

elif loading_percentage >= 65:

    st.warning(
        "⚠️ High Transformer Loading. "
        "AI Optimization Recommended."
    )

else:

    st.success(
        "🟢 Transformer Operating "
        "in Normal Condition."
    )


# ============================================================
# FOOTER
# ============================================================

st.markdown("---")

st.caption(
    "⚡ AI-Powered Smart Distribution Network | "
    "WattNext26 Project Competition"
)