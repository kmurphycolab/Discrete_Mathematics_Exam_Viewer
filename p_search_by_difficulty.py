import streamlit as st
from my_lib import *
from content import *


def build_page():
    st.header("Search questions by difficulty ...")

    with st.expander("What is difficulty?"):
        st.markdown(search_by_difficulty_intro)
        
    difficulty_options = list(range(1,6))

    difficulty_selected = st.radio("**Select difficulty to filter questions:**",
        [f"***{k}***" for k in difficulty.keys()],
        index=0, horizontal=True,
        # captions=[f"***{v}***" for v in difficulty.values()],
        help="**Difficulty level**\n" + "\n".join([f"{k}. {v}" for k,v in difficulty.items()])
    )

    difficulty_selected = difficulty_selected.replace("*","")
    questions = list(df.query(f"difficulty=={difficulty_selected}").index.values)

    if not questions:
        st.write("### No questions found matching selected difficulty")
        return
    
    if config['exclude_NA_questions']:
        questions = df.iloc[questions].query(f"{na_column}==False").index.values
    st.write(f"### Matching questions ({len(questions)})")  
    for idx, row in df.iloc[questions].iterrows():
        display_question(row, header=True)

build_sidebar()
build_page()