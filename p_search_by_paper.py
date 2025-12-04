import streamlit as st
from my_lib import *
from content import *


def build_page():
    st.header("Search questions by paper ...")

    with st.expander("Why?"):
        st.markdown(search_by_paper_intro)
        
    paper_options = sorted(df.paper.unique())
    
    paper_selected = st.selectbox("**Select paper to filter questions:**", options=paper_options, index=0)

    questions = list(df.query(f"paper=='{paper_selected}'").index.values)
    if not questions:
        st.write("### No questions found matching task")
        return
    
    if config['exclude_NA_questions']:
         questions = df.iloc[questions].query(f"`{na_column}`==False").index.values
    st.write(f"### Matching questions ({len(questions)})")  
    for idx, row in df.iloc[questions].iterrows():
        display_question(row, header=True)

build_sidebar()
build_page()