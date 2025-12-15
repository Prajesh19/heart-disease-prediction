import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle
import os

# Step 1: Load dataset
data = pd.read_csv("dataset/heart.csv")

# Step 2: Split features and target
X = data.drop("target", axis=1)
y = data["target"]

# Step 3: Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Normalize the data
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Step 5: Train the model
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# Step 6: Evaluate the model
y_pred = model.predict(X_test_scaled)
acc = accuracy_score(y_test, y_pred)
print(f"✅ Model Training Completed — Accuracy: {acc * 100:.2f}%")

# Step 7: Save model, scaler, and scaled training data
os.makedirs("model", exist_ok=True)
pickle.dump(model, open("model/heart_model.pkl", "wb"))
pickle.dump(scaler, open("model/scaler.pkl", "wb"))
pickle.dump(X_train_scaled, open("model/X_train_scaled.pkl", "wb"))
pickle.dump(y_train, open("model/y_train.pkl", "wb"))   # <-- ✅ Add this line

print("✅ All model files saved successfully in 'model/' folder (including y_train.pkl).")
