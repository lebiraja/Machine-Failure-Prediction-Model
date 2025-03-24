import streamlit as st
import numpy as np
import joblib

# Load the trained model and scaler
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

# Mapping Quality levels to numerical values
quality_mapping = {"L": 0, "M": 1, "H": 2}

# Streamlit UI
st.title("🔧 Machine Status Predictor")

st.markdown("Enter the machine parameters to check if it's **Normal** or a **Failure Detected**.")

# Input fields
quality = st.selectbox("Quality Level", ["L", "M", "H"])
ambient_t = st.number_input("Ambient Temperature (°C)", format="%.2f")
process_t = st.number_input("Process Temperature (°C)", format="%.2f")
rotation_speed = st.number_input("Rotation Speed (RPM)", format="%.2f")
torque = st.number_input("Torque (Nm)", format="%.2f")
tool_wear = st.number_input("Tool Wear (min)", format="%.2f")

# Prediction button
if st.button("🔍 Predict Machine Status"):
    try:
        # Convert quality level
        quality_num = quality_mapping[quality]

        # Prepare input for prediction
        new_sample = np.array([[quality_num, ambient_t, process_t, rotation_speed, torque, tool_wear]])
        new_sample_scaled = scaler.transform(new_sample)

        # Predict
        result = model.predict(new_sample_scaled)[0]
        status = "✅ Machine Status: **NORMAL**" if result == 0 else "⚠️ Machine Status: **FAILURE DETECTED!**"

        st.success(status)
    except Exception as e:
        st.error(f"Error: {e}")
