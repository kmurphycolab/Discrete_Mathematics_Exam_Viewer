import streamlit as st
from my_lib import *
from content import *
from streamlit_tree_select import tree_select

def build_page():
    st.header("Search questions by topic ...")

    with st.expander("What is a topic?"):
        st.markdown(search_by_topic_intro)

    nodes = []
    def add_entry(topic):
        entry = { "label": topic['name'].split("/")[-1], "value":topic['name'] }
        if topic['children']:
            entry['children'] = []
            for child in topic['children'].values():
                entry['children'].append(add_entry(child))
        return entry

    nodes = []
    for child in topics[MODULE]['children'].values():
        nodes.append(add_entry(child))

    st.write("**Select topic, or sub-topic or ...**")
    return_select = tree_select(nodes)
    # st.write(return_select)

    if not return_select['checked']: return

    questions = []
    for topic in return_select['checked']:
        # st.write(topic)
        node = topics[MODULE]
        for label in topic.split(" / ")[1:]:
            node = node['children'][label]
        questions += node['questions']

    # st.write(questions)
        
    if not questions:
        st.write("### No questions found matching topics selected")
        return

    if config['exclude_NA_questions']:
        questions = df.iloc[questions].query(f"{na_column}==False").index.values

    st.write(f"### Matching questions ({len(questions)})")  
    for idx, row in df.iloc[questions].iterrows():
        display_question(row, header=True)

build_sidebar()
build_page()