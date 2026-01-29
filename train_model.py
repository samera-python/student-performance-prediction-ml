import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

# Example training data
# Replace these with your actual dataset
X = np.array([
    [90, 80, 85, 5],
    [70, 60, 75, 3],
    [85, 78, 80, 4]
])
y = np.array([88, 68, 82])

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model with joblib
joblib.dump(model, "student_model.pkl")
print("Model saved successfully!")
