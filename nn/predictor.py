import tensorflow as tf
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import os

# get project root
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

model_path = os.path.join(BASE_DIR, "model", "grade_predictor.h5")
data_path = os.path.join(BASE_DIR, "data", "student_performance.csv")

# load model
model = tf.keras.models.load_model(model_path, compile=False)

# rebuild scaler
data = pd.read_csv(data_path)
X = data.drop("final_grade", axis=1)

scaler = MinMaxScaler()
scaler.fit(X)

def predict_grade(previous_gpa, attendance, study_hours, interest, difficulty, subject_type=0):

    # Include subject_type in features to match the scaler's expected columns
    features = pd.DataFrame([[
        previous_gpa, attendance, study_hours, interest, difficulty, subject_type
    ]], columns=X.columns)

    features_scaled = scaler.transform(features)

    grade = model.predict(features_scaled, verbose=0)[0][0]

    return round(float(max(0, min(10, grade))), 2)