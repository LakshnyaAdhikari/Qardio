import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report, confusion_matrix
import joblib
import os

# -----------------------------------------------
# 1. Load Dataset
# -----------------------------------------------
df = pd.read_csv('data.csv')
print("Dataset loaded!")

# -----------------------------------------------
# 2. Keep Only Needed Columns
# -----------------------------------------------
required_columns = [
    'age','ap_hi','ap_lo','weight','height','cholesterol','gluc',
    'smoke','alco','gender','active','disease'
]

df = df[required_columns]

# -----------------------------------------------
# 3. Handle Missing Values
# -----------------------------------------------
for col in df.columns:
    df[col] = df[col].fillna(df[col].mode()[0])

# -----------------------------------------------
# 4. Convert Age (days → years)
# -----------------------------------------------
df['age'] = (df['age'] / 365).astype(int)

# -----------------------------------------------
# 5. Add Computed Features
# -----------------------------------------------
df['BMI'] = df['weight'] / ((df['height'] / 100) ** 2)
df['pulse_pressure'] = df['ap_hi'] - df['ap_lo']

# -----------------------------------------------
# 6. Train/Test Split
# -----------------------------------------------
X = df.drop(columns=['disease'])
y = df['disease']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# -----------------------------------------------
# 7. Train Random Forest
# -----------------------------------------------
model = RandomForestClassifier(
    n_estimators=300,
    max_depth=12,
    random_state=42,
    class_weight='balanced'
)

print("Training Random Forest...")
model.fit(X_train, y_train)

# -----------------------------------------------
# 8. Evaluation
# -----------------------------------------------
y_pred = model.predict(X_test)

print("\nAccuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("F1 Score:", f1_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred))

# Save Confusion Matrix
plt.figure(figsize=(6,4))
sns.heatmap(confusion_matrix(y_test, y_pred), annot=True, fmt='d', cmap='Purples')
plt.title("Random Forest - Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.savefig("confusion_matrix.png")
plt.close()

# -----------------------------------------------
# 9. Save Model
# -----------------------------------------------
os.makedirs("model", exist_ok=True)
joblib.dump(model, "model/model.pkl")

print("\n🎉 Model saved successfully!")
