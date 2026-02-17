from fuzzy.fuzzy_system import classify_student

student_type = classify_student(
    previous_gpa=7.2,
    attendance=8,
    study_hours=7
)

print("Student Type:", student_type)