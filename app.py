import streamlit as st
import pandas as pd
from fuzzy.fuzzy_system import classify_student
from optimization.pso_scheduler import run_pso

st.set_page_config(page_title="AI Course Advisor", layout="centered")

st.title("Adaptive Course Advisor")

st.write("Enter your academic details")

# -------- Inputs --------
gpa = st.slider("Previous GPA", 0.0, 10.0, 7.0, 0.1)
attendance = st.slider("Attendance Level", 0.0, 10.0, 8.0, 0.1)
study = st.slider("Study Effort", 0.0, 10.0, 7.0, 0.1)
interest = st.slider("Interest Level", 0.0, 10.0, 8.0, 0.1)

if st.button("Generate Recommendation"):

    student = {
        "gpa": gpa,
        "attendance": attendance,
        "study": study,
        "interest": interest
    }

    # Fuzzy classification
    student_type = classify_student(gpa, attendance, study)

    # Optimization
    best_plan, predicted_gpa = run_pso(student, student_type)

    subjects = pd.read_csv("data/subjects.csv")

    st.subheader("Student Type")
    st.success(student_type)

    st.subheader("Recommended Subjects")
    # Display recommended subjects with additional details in a table
    recommended_df = subjects.iloc[best_plan][["subject", "difficulty", "credits", "category"]]
    st.table(recommended_df.reset_index(drop=True))

    st.subheader("Expected GPA")
    st.info(round(predicted_gpa, 2))

    if student_type == "Weak":
        st.warning("Advice: Focus on manageable workload")
    elif student_type == "Average":
        st.warning("Advice: Balanced difficulty recommended")
    else:
        st.warning("Advice: You can handle challenging subjects")