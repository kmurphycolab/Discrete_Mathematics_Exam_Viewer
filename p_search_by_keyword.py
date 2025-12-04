import streamlit as st
from my_lib import *
from content import *


def build_page():
    st.header("Search questions by keyword ...")

    with st.expander("What is a keyword?"):
        st.markdown(search_by_keyword_intro)

    keywords_options = sorted(keywords.keys())

    keywords_selected = st.multiselect("**Select keywords to filter questions:**", keywords_options)
    keywords_mode = st.radio("**Select mode to treat multiple keywords:**",
        ["***AND***", "***OR***"],
        horizontal=True, index=0,
        captions=[
            "Find questions that contain all selected keywords.",
            "Find questions that contain some selected keywords.",
            ]
        )
    # st.write("You selected:", keywords_selected)

    if not keywords_selected: return
    
    if keywords_mode=="***AND***":
        results = set(df.index.values)
        for keyword in keywords_selected:
            if DEBUG: st.write(f"{keyword = } {keywords[keyword] = }")
            results &= set(keywords[keyword])
    else:
        results = set()
        for keyword in keywords_selected:
            if DEBUG: st.write(f"{keyword = } {keywords[keyword] = }")
            results |= set(keywords[keyword])

    questions = sorted(results)

    if not questions:
        st.write("### No questions found matching keyword criteria")
        return

    if config['exclude_NA_questions']:
        questions = df.iloc[questions].query(f"{na_column}==False").index.values

    st.write(f"### Matching questions ({len(questions)})")  
    for idx, row in df.iloc[questions].iterrows():
        display_question(row, header=True)



build_sidebar()
build_page()
