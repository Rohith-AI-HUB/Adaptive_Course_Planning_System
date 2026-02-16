from optimization.pso_scheduler import run_pso
from fuzzy.fuzzy_system import classify_student
import pandas as pd

student = {
    "gpa": 7.5,
    "attendance": 8,
    "study": 7,
    "interest": 8
}

stype = classify_student(student["gpa"], student["attendance"], student["study"])

plan, score = run_pso(student, stype)

subjects = pd.read_csv("data/subjects.csv")

print("Student Type:", stype)
print("Recommended Subjects:")

for i in plan:
    print("-", subjects.iloc[i]["subject"])

print("Expected GPA:", round(score,2))