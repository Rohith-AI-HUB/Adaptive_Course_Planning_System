import os
import pandas as pd
import random
from nn.predictor import predict_grade

MAX_CREDITS = 18
NUM_SUBJECTS = 4
ITERATIONS = 30
PARTICLES = 20

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "subjects.csv")
subjects = pd.read_csv(DATA_PATH)
grade_cache = {}
# ----------------------------------

def get_subject_grade(subject_idx, student):

    # unique key per student + subject
    key = (
        subject_idx,
        round(student["gpa"],2),
        round(student["attendance"],2),
        round(student["study"],2),
        round(student["interest"],2)
    )

    if key in grade_cache:
        return grade_cache[key]

    row = subjects.iloc[subject_idx]

    grade = predict_grade(
        student["gpa"],
        student["attendance"],
        student["study"],
        student["interest"],
        row["difficulty"]
    )

    grade_cache[key] = grade
    return grade



def evaluate_plan(plan, student, student_type):

    total_credits = 0
    grades = []

    for idx in plan:
        row = subjects.iloc[idx]

        grade = get_subject_grade(idx, student)

        grades.append(grade)
        total_credits += row["credits"]

    if total_credits > MAX_CREDITS:
        return -100

    avg = sum(grades) / len(grades)

    if student_type == "Weak":
        hard = sum(subjects.iloc[i]["difficulty"] > 7 for i in plan)
        avg -= hard * 0.7

    return avg


# ----------------------------------

def random_particle():
    return random.sample(range(len(subjects)), NUM_SUBJECTS)


def run_pso(student, student_type):

    grade_cache.clear()

    swarm = [random_particle() for _ in range(PARTICLES)]
    best_global = None
    best_score = -999

    for _ in range(ITERATIONS):

        for particle in swarm:

            score = evaluate_plan(particle, student, student_type)

            if score > best_score:
                best_score = score
                best_global = particle.copy()

        # mutate particles towards best
        for i in range(PARTICLES):
            if random.random() < 0.5:
                swap_idx = random.randint(0, NUM_SUBJECTS-1)
                candidate = best_global[swap_idx]

                # avoid duplicates
                if candidate not in swarm[i]:
                    swarm[i][swap_idx] = candidate
                else:
                    # random replace instead
                    available = list(set(range(len(subjects))) - set(swarm[i]))
                    if available:
                        swarm[i][swap_idx] = random.choice(available)

    return best_global, best_score