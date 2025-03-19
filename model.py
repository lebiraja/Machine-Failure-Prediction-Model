import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from imblearn.over_sampling import SMOTE

# Load CSV file
file_path = "factory_data (classification).csv"  # Change this to your actual file path
df = pd.read_csv(file_path)

# Handle Missing Values
df.dropna(inplace=True)  # Remove rows with NaN values
# df.fillna(df.mean(), inplace=True)  # OR fill NaNs with column mean

# Drop Unique ID & Product ID (not useful for prediction)
df.drop(columns=["Unique ID", "Product ID"], inplace=True)

# Encode categorical column "Quality"
le = LabelEncoder()
df["Quality"] = le.fit_transform(df["Quality"])  # Converts L, M, H to numerical values

# Separate features (X) and target (y)
X = df.drop(columns=["Machine Status"])
y = df["Machine Status"]

# Standardize numeric features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Handle class imbalance with SMOTE
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_scaled, y)

# Split into train & test sets
X_train, X_test, y_train, y_test = train_test_split(X_resampled, y_resampled, test_size=0.2, random_state=42)

# Train Random Forest model with class balancing
model = RandomForestClassifier(class_weight="balanced", random_state=42)
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy:.2f}")
print("Classification Report:\n", classification_report(y_test, y_pred))
