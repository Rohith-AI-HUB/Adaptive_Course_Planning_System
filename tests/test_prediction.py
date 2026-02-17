from nn.predictor import predict_grade

grade = predict_grade(
    previous_gpa=7.5,
    attendance=8,
    study_hours=7,
    interest=9,
    difficulty=6
)

print("Predicted Grade:", grade)