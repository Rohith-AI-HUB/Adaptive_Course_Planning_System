import random
import csv

def clamp(x):
    return max(0, min(10, round(x,2)))

rows = []

for _ in range(800):

    previous_gpa = random.uniform(4, 9.8)
    attendance = random.uniform(3, 10)
    study_hours = random.uniform(2, 10)
    interest = random.uniform(1, 10)
    difficulty = random.uniform(3, 10)

    # NEW FEATURE
    subject_type = random.choice([0,1])  
    # 0 = theory, 1 = practical

    # student learning style
    practical_skill = random.uniform(1,10)

    base = (
        0.35*previous_gpa +
        0.30*study_hours +
        0.20*attendance +
        0.15*interest
    )

    difficulty_penalty = difficulty * 0.08

    # affinity effect
    if subject_type == 1:
        affinity_bonus = practical_skill * 0.15
    else:
        affinity_bonus = (10-practical_skill) * 0.15

    grade = base - difficulty_penalty + affinity_bonus + random.uniform(-0.5,0.5)

    grade = clamp(grade)

    rows.append([
        previous_gpa, attendance, study_hours, interest,
        difficulty, subject_type, grade
    ])

with open("data/student_performance.csv","w",newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "previous_gpa","attendance","study_hours","interest",
        "difficulty","subject_type","final_grade"
    ])
    writer.writerows(rows)

print("Dataset regenerated with subject affinity")