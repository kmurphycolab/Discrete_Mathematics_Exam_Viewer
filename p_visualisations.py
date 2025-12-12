import streamlit as st
from my_lib import *
from content import *
import plotly.express as px

from topics import *

def build_page():

    df_tmp = df.copy()

    st.header("Past Papers Statistics")

    st.write("### Breakdown of past papers by topic")

    st.write("""Note that there is no topic 
        "Computational Thinking" since that appears 
        across all other topics in the python questions. 
        So search by keyword "python" to find these questions.""")
    df_tmp['topic'] = df_tmp['topic'].apply(lambda s: s.split("/")[0].strip())

    df_tmp = df_tmp.groupby(["paper","topic"])[['mark']].sum().reset_index()

    fig = px.bar(
        df_tmp,
        x="paper",
        y="mark",
        color="topic",
        barmode="stack",
        category_orders={"topic": topics_info.keys()} 
    )

    st.plotly_chart(fig, use_container_width=True)

    pass

build_page()