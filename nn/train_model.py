import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
import os

# Load dataset
data = pd.read_csv("../data/student_performance.csv")

X = data.drop("final_grade", axis=1)
y = data["final_grade"]

# Normalize inputs
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# Build Neural Network
model = tf.keras.Sequential([
    tf.keras.layers.Dense(16, activation='relu', input_shape=(6,)),
    tf.keras.layers.Dense(8, activation='relu'),
    tf.keras.layers.Dense(1)
])

model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.01),
    loss='mse',
    metrics=['mae']
)

# Train
model.fit(X_train, y_train, epochs=100, verbose=1)

# Evaluate
loss, mae = model.evaluate(X_test, y_test)
print("Test MAE:", mae)

# Save model
os.makedirs("../model", exist_ok=True)
model.save("../model/grade_predictor.h5")

print("Model saved successfully")