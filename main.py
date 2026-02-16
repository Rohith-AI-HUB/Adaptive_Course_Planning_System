from fuzzy.fuzzy_system import classify_student
from optimization.pso_scheduler import run_pso
import pandas as pd

# -------- Student Input --------
student = {
    "gpa": float(input("Enter previous GPA (0-10): ")),
    "attendance": float(input("Enter attendance (0-10): ")),
    "study": float(input("Enter study effort (0-10): ")),
    "interest": float(input("Enter interest level (0-10): "))
}

# -------- Fuzzy Classification --------
student_type = classify_student(
    student["gpa"],
    student["attendance"],
    student["study"]
)

# -------- Optimization --------
best_plan, predicted_gpa = run_pso(student, student_type)

subjects = pd.read_csv("data/subjects.csv")

# -------- Output --------
print("\n===== AI COURSE ADVISOR =====")
print("Student Type:", student_type)

print("\nRecommended Subjects:")
for i in best_plan:
    print("-", subjects.iloc[i]["subject"])

print("\nExpected Semester GPA:", round(predicted_gpa,2))

if student_type == "Weak":
    print("Advice: Focus on fundamentals and manageable workload")
elif student_type == "Average":
    print("Advice: Balanced difficulty recommended")
else:
    print("Advice: You can handle challenging subjects")