def triangular(x, a, b, c):
    if x <= a or x >= c:
        return 0
    elif x == b:
        return 1
    elif x < b:
        return (x - a) / (b - a)
    else:
        return (c - x) / (c - b)


# Membership functions
def gpa_low(x): return triangular(x, 0, 4, 6)
def gpa_medium(x): return triangular(x, 5, 7, 8.5)
def gpa_high(x): return triangular(x, 7.5, 9, 10)

def attendance_low(x): return triangular(x, 0, 4, 6)
def attendance_medium(x): return triangular(x, 5, 7, 8.5)
def attendance_high(x): return triangular(x, 7.5, 9, 10)

def study_low(x): return triangular(x, 0, 3, 5)
def study_medium(x): return triangular(x, 4, 6, 8)
def study_high(x): return triangular(x, 7, 9, 10)


def classify_student(previous_gpa, attendance, study_hours):

    # Rule strengths
    strong = max(
        min(gpa_high(previous_gpa), study_high(study_hours)),
        min(gpa_high(previous_gpa), attendance_high(attendance))
    )

    weak = max(
        gpa_low(previous_gpa),
        attendance_low(attendance)
    )

    average = max(
        min(gpa_medium(previous_gpa), study_medium(study_hours)),
        min(gpa_medium(previous_gpa), attendance_medium(attendance))
    )

    # Decision
    if strong >= average and strong >= weak:
        return "Strong"
    elif weak >= strong and weak >= average:
        return "Weak"
    else:
        return "Average"