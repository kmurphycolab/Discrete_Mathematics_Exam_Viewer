import streamlit as st
from my_lib import *
from content import *

def build_page():
    st.header("Past exam papers ...")

    for paper in df.paper.unique():
        st.write(f"### {paper}")

        cols = st.columns(2)
        with cols[0]:
            download_exam_button(paper)
        with cols[1]:
            download_ms_button(paper)
build_page()
