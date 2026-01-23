import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load dataset
data = pd.read_csv("peak_training_data.csv")

# Encode categorical columns
encoders = {}
categorical_cols = ["mood", "time_of_day", "problem", "coping", "output"]

for col in categorical_cols:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    encoders[col] = le

# Features and target
X = data.drop("output", axis=1)
y = data["output"]

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

# Save trained model + encoders
with open("peak_model.pkl", "wb") as f:
    pickle.dump((model, encoders), f)

print("✅ Peak Performance ML model trained successfully!")
