import streamlit as st

from my_lib import *

st.set_page_config(
    page_title="Discrete Mathematics Study Guide",
    page_icon="📕",
)

pg = st.navigation([
    st.Page("p_intro.py", title="Introduction", icon="💁‍♂️"),
    st.Page("p_search_by_topic.py", title="Search by Topic", icon="🔎"),
    st.Page("p_search_by_task.py", title="Search by Task", icon="🔎"),
    st.Page("p_search_by_keyword.py", title="Search by Keyword", icon="🔎"),
    st.Page("p_search_by_difficulty.py", title="Search by Difficulty", icon="🔎"),
    st.Page("p_search_by_paper.py", title="Search by Paper", icon="🔎"),
    st.Page("p_exam_papers.py", title="Exam Papers", icon="📕"),
    st.Page("p_predict_my_grade.py", title="Predict my Grade", icon="🔥"),
])
pg.run()

