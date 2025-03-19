import numpy as np
import joblib

# Load trained model and scaler
model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")  

# Mapping Quality levels to numerical values (as done in training)
quality_mapping = {"L": 0, "M": 1, "H": 2}

# Get user input
quality = input("Enter Quality (L/M/H): ").strip().upper()
ambient_t = float(input("Enter Ambient Temperature (C): "))
process_t = float(input("Enter Process Temperature (C): "))
rotation_speed = float(input("Enter Rotation Speed (rpm): "))
torque = float(input("Enter Torque (Nm): "))
tool_wear = float(input("Enter Tool Wear (min): "))

# Convert Quality to a numerical value
if quality not in quality_mapping:
    print("❌ Invalid Quality! Enter L, M, or H.")
    exit()

quality_num = quality_mapping[quality]

# Prepare input with 6 features
new_sample = np.array([[quality_num, ambient_t, process_t, rotation_speed, torque, tool_wear]])

# Standardize input using the same scaler from training
new_sample_scaled = scaler.transform(new_sample)

# Predict
prediction = model.predict(new_sample_scaled)

# Output result
if prediction[0] == 0:
    print("\n🔹 Machine Status: NORMAL")
else:
    print("\n⚠️ Machine Status: FAILURE DETECTED!")
