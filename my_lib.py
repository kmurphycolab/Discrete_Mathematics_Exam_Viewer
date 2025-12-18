import streamlit as st

import pandas as pd
import fitz
import base64
import numpy as np
from pathlib import Path
from collections import defaultdict

MODULE = "Discrete Mathematics"
na_column = "NA_202526"

DEBUG = False

config = {
    'show_question_detail': True,
    'exclude_NA_questions': True,
}

def exam_label_to_key(s):
    if "/" in s:
        a_year, version = s.split(" ")
        a_year = a_year[:4] + a_year[5:]
        return f"{a_year}_{version}"
    return s


def get_paper(s):

    key = exam_label_to_key(s)

    return fitz.open(f"papers/{MODULE.replace(' ','_')}_{key}_E.pdf")
    # return fitz.open(f"papers/grid.pdf")

def get_question(data, x_margin=20, y_offset=0):

    paper = get_paper(data.paper)
    page = paper[data.page]
    top, bottom = data.top, data.bottom
    rect = fitz.Rect(x_margin, (top+y_offset)*842/100, 595-x_margin, (bottom+y_offset)*842/100)
    question = page.get_pixmap(clip=rect, dpi=150)

    return question


@st.fragment
def download_exam_button(label: str):
    key = exam_label_to_key(label)
    filename = f"{MODULE.replace(' ','_')}_{key}_E.pdf"

    filepath = Path(f"papers/{filename}")
    if not filepath.exists(): return 

    with open(filepath, "rb") as f:
        pdf_bytes = f.read()

    st.download_button(
        label="Download Exam Paper",
        data=pdf_bytes,
        file_name="example.pdf",
        mime="application/pdf",
        key=np.random.randint(1,2<<30),
    )

@st.fragment
def download_ms_button(label: str):
    key = exam_label_to_key(label)
    filename = f"{MODULE.replace(' ','_')}_{key}_MS.pdf"

    filepath = Path(f"papers/{filename}")
    if not filepath.exists(): return 

    with open(filepath, "rb") as f:
        pdf_bytes = f.read()

    st.download_button(
        label="Download Marking Scheme",
        data=pdf_bytes,
        file_name=filename,
        mime="application/pdf",
        key=np.random.randint(1,2<<30),
    )

def display_question(data, header=True, detail=True):
    if header:
        note = ":red[(not applicable for 2025/26 exams)]" if data[na_column] else ""
        st.write(f"#### {data.paper} &mdash; {data.question} {note}")
    if detail and config['show_question_detail']:
        st.markdown(f""" 
* **Topic:** {data.topic}
* **Tasks:** {data.tasks}
* **Keywords:** {data.keywords}
* **Difficulty:** {data.difficulty}
* **Applicable for 2025/26:** {not data[na_column]}          
"""
 + (f"* **Comment:** {data.comment}\n" if data.comment else "")
 + (f"* :red[**Warning:** {data.error}]\n" if data.error else "")
)
        
    question = get_question(data)
    png_bytes = question.tobytes("png")
    b64 = base64.b64encode(png_bytes).decode()


    html = f"""
<div style="
    border: 3px solid #444;
    padding: 6px;
    display: inline-block;
">
    <img src="data:image/png;base64,{b64}" style="display:block;">
</div>
"""
    st.markdown(html, unsafe_allow_html=True)

    cols = st.columns(2)
    with cols[0]:
        download_exam_button(data.paper)
    with cols[1]:
        download_ms_button(data.paper)


# common processing
    

df = pd.read_excel("questions.xlsx").fillna("")
for c in ['page', 'top', 'bottom']:
    df[c] = df[c].astype(int)
df[na_column] = (df[na_column]=="YES")

# topics

DEBUG = False

topics = {MODULE: 
    {'name': MODULE, 
    'children': {
        'logic': {'name':f"{MODULE} / logic", 'children':{}, 'questions':[]},
        'collections': {'name':f"{MODULE} / collections", 'children':{}, 'questions':[]},
        'relations': {'name':f"{MODULE} / relations", 'children':{}, 'questions':[]},
        'functions': {'name':f"{MODULE} / functions", 'children':{}, 'questions':[]},
        'enumeration': {'name':f"{MODULE} / enumeration", 'children':{}, 'questions':[]},
        'graphs': {'name':f"{MODULE} / graphs", 'children':{}, 'questions':[]},
    }, 
    'questions':[]} 
}

# topics = { MODULE: {'name': MODULE, 'children': {}, 'questions':[] } } 
# for topic in row.topic.split("/"):   

def populate_topics(df, questions=False):
    for idx, row in df.iterrows():
        parent = topics[MODULE]
        if DEBUG: st.write(f"At topic {parent['name']} with {len(parent['children'])} children and {len(parent['questions'])} questions")
        if DEBUG: st.write(f"{row.topic = }")
        for topic in row.topic.split("/"):
            topic = topic.strip()
            if DEBUG: st.write(f"Parent {parent['name']} with {len(parent['children'])} children and {len(parent['questions'])} questions")
            if topic not in parent['children']:
                parent['children'][topic] = {'name':f"{parent['name']} / {topic}", 'children':{}, 'questions':[]}
                if DEBUG: st.write(f"At topic {parent['name']} with {len(parent['children'])} children and {len(parent['questions'])} questions")
            parent = parent['children'][topic]
        if questions:
            parent['questions'].append(idx)

populate_topics(df, questions=True)

DEBUG = False

# tasks

tasks = defaultdict(list)        
for idx, row in df.iterrows():
    for task in row.tasks.split("."):
        task = task.strip()
        if not task: continue
        if not task.endswith("."): task += "."
        tasks[task].append(idx)
tasks = dict(sorted(tasks.items()))

# keywords
    
keywords = defaultdict(list)
for idx, row in df.iterrows():
    for keyword in row.keywords.split(","):
        keyword = keyword.strip()
        keywords[keyword].append(idx)

# build common UI elements

def build_sidebar():    
    global config
    # st.sidebar.markdown("---")
    config['show_question_detail'] = st.sidebar.checkbox("Show question detail", value=True)
    config['exclude_NA_questions'] = st.sidebar.checkbox("Exclude NA questions", value=True)
