import streamlit as st
from my_lib import *
from content import *
from numpy.random import default_rng

from tasks import *

skills = {
    "Not a clue":                      [0.3, 0.1, 0.0, 0.0, 0.0],
    "I usually get it mostly wrong":   [0.5, 0.4, 0.2, 0.0, 0.0],
    "I'm OK":                          [0.7, 0.5, 0.4, 0.2, 0.1],
    "I usually get it mostly correct": [1.0, 0.8, 0.5, 0.3, 0.2],
    "I'm well sorted":                 [1.0, 1.0, 0.9, 0.8, 0.6],
}

N_SIMULATION = 100

def predict_grade(paper, task_skill_level, seed=None):

    rng = default_rng(seed)

    grade = 0
    df_paper = df.query(f"paper=='{paper}'")
    for idx, row in df_paper.iterrows():
        tasks = [
            (t.strip() if t.endswith(".") else t.strip()+".")
            for t in row.tasks.split(".") if t.strip()
        ]
        for task in tasks:
            pr_correct = skills[task_skill_level[task]][row.difficulty-1]
            pr_correct = np.clip(pr_correct+rng.normal(scale=0.1),0,1)
            grade += row.mark * pr_correct / len(tasks)

    return grade

    
def build_page():
    st.header("An absolutely horrible grade predictor ...")

    with st.expander("What is this doing?"):
        st.markdown(grade_predictor_intro)
   
    st.write("**For each of the following tasks, indicate your ability ...**")
    task_skill_level = {}
    for task in tasks:
        if task in task_info:
            help = f"##### Task: {task}\n\n" + task_info[task]['summary']
        else:
            help = None
        task_skill_level[task] = st.select_slider(task,skills.keys(), key=task, help=help)

    st.write(f"## Predicted performance on past papers ...")
    for paper in sorted(df.paper.unique()):
        scores = [predict_grade(paper, task_skill_level)
            for _ in range(N_SIMULATION)]
        st.write(f"### {paper}")
        st.write(f"A simulation, of {N_SIMULATION} iterations, generated grades in the interval ({np.min(scores):.0f}%, {np.max(scores):.0f}%) with an average of {np.mean(scores):.0f}%.")
build_sidebar()
build_page()