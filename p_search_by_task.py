import streamlit as st
from my_lib import *
from content import *


def build_page():
    st.header("Search questions by task ...")

    with st.expander("What is a task?"):
        st.markdown(search_by_task_intro)
        
    task_options = sorted(tasks.keys())

    task_selected = st.selectbox("**Select task to filter questions:**", options=task_options, index=0)

    questions = sorted(tasks[task_selected])
    
    if not questions:
        st.write("### No questions found matching task")
        return
    
    if config['exclude_NA_questions']:
        questions = df.iloc[questions].query(f"{na_column}==False").index.values
    st.write(f"### Matching questions ({len(questions)})")  
    for idx, row in df.iloc[questions].iterrows():
        display_question(row, header=True)

build_sidebar()
build_page()