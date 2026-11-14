 ⚡ AI-Powered Intelligent Load Forecasting and Energy Management System
 
An AI-powered smart grid system using CNN-LSTM load forecasting and Deep Reinforcement Learning (DQN) for intelligent energy management.

The system integrates Federated Learning, Explainable AI, EV Charging Optimization, Renewable Energy Management, and Transformer Load Monitoring for smart distribution networks.

 🎯 Project Overview

Modern electrical distribution networks face challenges due to:

 Increasing electricity demand

 Peak load conditions

 Electric Vehicle (EV) charging demand

 Renewable energy intermittency

 Transformer overloading

 Consumer data privacy



This project proposes an AI-powered intelligent energy management system that predicts electrical load and dynamically selects grid control actions.

Key Technologies

| Technology | Application |

| CNN-LSTM | Electrical Load Forecasting |

| Deep Reinforcement Learning | Energy Management |

| DQN | Intelligent Grid Action Selection |

| Federated Learning | Privacy-Preserving Distributed AI |

| Explainable AI | Feature Importance and Model Interpretation |

| Streamlit | Interactive Smart Grid Dashboard |

| TensorFlow | Deep Learning Model Development |

| Plotly | Interactive Data Visualization |
 System Architecture

Smart Meters / Distributed Grid Nodes

                │

                ▼

       Federated Learning Layer

                │

                ▼

        CNN-LSTM Forecasting

                │

                ▼

       Forecasted Grid Load

                │

                ▼

   Deep Reinforcement Learning

           DQN Agent

                │

                ▼

      Intelligent Grid Actions

       ┌────────┼────────┐

       ▼        ▼        ▼

    Battery    EV      Renewable

    Control  Charging    Energy

                │

                ▼

      Explainable AI Layer

                │

                ▼

     Streamlit Smart Grid Dashboard

 📈 AI Load Forecasting

The forecasting layer uses a CNN-LSTM deep learning model.

 CNN
The Convolutional Neural Network identifies local patterns in electrical load data.

 LSTM

The Long Short-Term Memory network learns temporal dependencies and load variations over time.

The model predicts future electrical demand using historical smart grid data.

Model Performance

Model: CNN-LSTM

R² Score: 0.6282

Deep Reinforcement Learning Energy Management



A Deep Q-Network (DQN) is used to perform intelligent energy management.

The DQN agent observes the smart grid state and selects an appropriate grid action.

 DRL State Variables

Forecast Load

Hour

Solar Generation

Wind Generation

EV Demand

 Available DQN Actions



| Action | Grid Decision |


| 0 | Normal Operation |

| 1 | Battery Discharge |

| 2 | Delay EV Charging |

| 3 | Use Renewable Energy |



The trained policy dynamically selects different actions based on grid operating conditions.

 📊 DQN Policy Analysis

The trained DQN model demonstrated a distributed action policy:

Action 0 | Normal Operation       | Selected 240 times

Action 1 | Battery Discharge      | Selected 506 times

Action 2 | Delay EV Charging      | Selected 223 times

Action 3 | Use Renewable Energy   | Selected 244 times

This demonstrates that the model can select different grid management actions instead of repeatedly selecting a single action.

 🌐 Federated Learning

Federated Learning enables distributed smart meters to participate in AI model training.

Workflow

1. Smart Meter A trains a local model.

2. Smart Meter B trains a local model.

3. Smart Meter C trains a local model.

4. Local model updates are sent to the central server.

5. Raw consumer data remains at the local smart meter.

6. The server aggregates local model updates.

This architecture supports  privacy-preserving distributed AI training.

💡 Explainable AI

The project includes an Explainable AI layer for understanding model behavior.

Feature importance analysis evaluates the influence of:

 Hour

 Day

 Month

 Year

 Temperature

 Solar Generation

 Wind Generation

 EV Demand

The dashboard also calculates a forecast confidence score using actual and forecast load error.

🔋 Battery Energy Management

The DQN agent can select Battery Discharge during suitable grid conditions.

Battery energy can support the grid during increased electrical demand and reduce stress on the distribution network.

 🚗 EV Charging Optimization

The DRL system monitors EV demand.

When required, the DQN agent can select:

Delay EV Charging

This supports EV load shifting and reduces additional grid stress.

 Renewable Energy Management

The system monitors:



\- Solar Generation

\- Wind Generation



The DQN agent can select:



```text

Use Renewable Energy

```



This improves renewable energy utilization in the smart distribution network.



\---



\## 🚨 Transformer Overload Monitoring



Transformer loading is calculated using forecasted electrical demand.



```text

Transformer Loading (%) =

Forecast Load / Transformer Capacity × 100

```



The monitoring system provides:



\- 🟢 Normal Condition

\- 🟡 High Transformer Loading

\- 🔴 Transformer Overload Alert



\---



\## 🖥️ Smart Grid Dashboard



The Streamlit dashboard provides:



\- Real-time smart grid simulation

\- Hour-based simulation control

\- Actual vs forecast load graph

\- CNN-LSTM model performance

\- Federated Learning workflow

\- DQN action visualization

\- Battery control status

\- EV charging status

\- Renewable energy status

\- Explainable AI feature importance

\- AI confidence score

\- Transformer overload monitoring



\---



\## 📁 Project Structure



```text

AI\_Smart\_Grid/

│

├── app.py

├── requirements.txt

├── README.md

│

├── data/

│   ├── raw/

│   ├── processed/

│   └── federated/

│

├── forecasting/

│   ├── train\_model.py

│   ├── predict.py

│   └── evaluate.py

│

├── federated\_learning/

│   ├── client1.py

│   ├── client2.py

│   ├── client3.py

│   ├── server.py

│   └── split\_data.py

│

├── reinforcement\_learning/

│   ├── dqn\_agent.py

│   ├── drl\_environment.py

│   ├── train\_drl.py

│   └── check\_policy.py

│

├── explainable\_ai/

│   ├── feature\_importance.py

│   ├── shap\_analysis.py

│   ├── confidence.py

│   └── recommendation.py

│

├── models/

│   ├── cnn\_lstm\_model.keras

│   └── dqn\_energy\_management.keras

│

└── results/

&#x20;   ├── load\_forecast.csv

&#x20;   ├── forecast\_graph.png

&#x20;   └── feature\_importance.png

```



\---



\## ⚙️ Installation



Clone the repository:



```bash

git clone https://github.com/keerthikakaruna2005-coder/AI-Smart-Grid-Energy-Management.git

```



Move to the project folder:



```bash

cd AI-Smart-Grid-Energy-Management

```



Create a virtual environment:



```bash

python -m venv venv

```



Activate the virtual environment on Windows:



```powershell

.\\venv\\Scripts\\Activate.ps1

```



Install dependencies:



```bash

pip install -r requirements.txt

```



\---



\## ▶️ Run the Dashboard



Run:



```bash

streamlit run app.py

```



The Streamlit smart grid dashboard will open in the browser.



\---



\## 🛠️ Tech Stack



\- Python

\- TensorFlow

\- Keras

\- Pandas

\- NumPy

\- Scikit-learn

\- Streamlit

\- Plotly

\- SHAP

\- Git

\- GitHub



\---



\## 🎓 Project Information



\*\*Project Title:\*\* AI-Powered Intelligent Load Forecasting and Energy Management System for Smart Distribution Networks



\*\*Competition:\*\* WattNext26 Project Competition



\*\*Department:\*\* Electrical and Electronics Engineering



\*\*Institution:\*\* University College of Engineering Kanchipuram, Anna University



\---



\## 👩‍💻 Developer



\*\*Keerthika K\*\*



B.E. Electrical and Electronics Engineering  

University College of Engineering Kanchipuram  

Anna University



\---



\## 🚀 Future Enhancements



\- Real-time IoT smart meter integration

\- Hardware-based smart grid prototype

\- Live weather API integration

\- Battery State of Charge monitoring

\- Multi-agent reinforcement learning

\- Advanced SHAP visualization

\- Cloud deployment

\- SCADA integration



\---



\## ⭐ Support



If you find this project useful, consider giving the repository a ⭐.

