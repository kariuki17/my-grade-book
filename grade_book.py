import streamlit as st

def add_score(scores, score):
    scores.append(score)
    return scores

def get_average(scores):
    if not scores:
        return 0
    return sum(scores) / len(scores)

def get_letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

def view_grades(scores):
    if not scores:
        return "No scores recorded yet."
    return "Scores: " + ", ".join(str(score) for score in scores)

st.title("Grade Book App")

# Store scores in session state
if "scores" not in st.session_state:
    st.session_state.scores = []

student_name = st.text_input("Enter student name:")

score_input = st.number_input("Enter score (0-100):", min_value=0.0, max_value=100.0, step=1.0)
if st.button("Add Score"):
    st.session_state.scores = add_score(st.session_state.scores, score_input)
    st.success("Score added successfully!")

st.subheader("Grades Overview")
st.write(view_grades(st.session_state.scores))

if st.session_state.scores:
    average = get_average(st.session_state.scores)
    letter_grade = get_letter_grade(average)
    
    st.write(f"Average Score: {average:.2f}")
    st.write(f"Letter Grade: {letter_grade}")

if st.button("Reset Scores"):
    st.session_state.scores = []
    st.success("Scores reset successfully!")
