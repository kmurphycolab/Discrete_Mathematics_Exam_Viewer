import streamlit as st
from my_lib import *
from content import *


st.header(f"{MODULE} Exam Guide")

st.markdown(f"""
This is an attempt to help you prepare for your {MODULE} exam by 
providing some structure to questions in past exam papers.

But first this app should come with a long list of disclaimers: 

1. Performance on past exam papers is no guarantee of performance on future exam papers.
2. This is an experiment and is a first iteration, so I might have coded some questions incorrectly. (I would be delighted if people send me corrections.)
3. The grade prediction calculator is probably worthless. 
""")

st.markdown(f"""
### Classification of past exam questions

We have different ways of studying so it is unlikely that there is a classification of questions that would suit everybody. So we have the following:
""")

st.page_link("p_search_by_topic.py", label="... by Topic", icon="🔎")
st.write("Questions are in a single topic. This roughly follows the structure used in the notes.")

st.page_link("p_search_by_task.py", label="... by Task", icon="🔎")
st.write("Questions are grouped based on the general process (sequence of steps) such as '_Construct a truth table._', etc., that you need to do.")

st.page_link("p_search_by_keyword.py", label="... by Keyword", icon="🔎")
st.write("Questions are keyword used in the questions of concepts needed to answer them.")

st.page_link("p_search_by_difficulty.py", label="... by Difficulty", icon="🔎")
st.write("Difficulty is a crude and subjective scale from 1 to 5.")

st.page_link("p_search_by_paper.py", label="... by Paper", icon="🔎")
st.write("I'm not going to write an explanation for this ... too late done ... feck.")

st.markdown(f"""
### Variations in module delivery over the years

While this module has been running for a long time, its structure has changed and each year there is a slight drift as we tweak topics or try new things.  So some past exam questions will not be applicable because we did not cover that concept/task/topic this year. Such question are flagged as "not applicable for 2025/26". Again, this was done quickly so if you see issues, then please contact us.
""")

st.markdown(f"""### Grade prediction calculator""")

st.page_link("p_predict_my_grade.py", label="Predict my Grade", icon="🔥")

st.markdown(f"""    
This is an attempt to estimate how well you would have done on a past paper, given your estimation of how well you can complete the various tasks.  

It is not at all reliable or even validated. There is little good to be said about it other than it kept me off social media while I was writing it.
""")


st.markdown(f"""  
### Version History
            
**0.2 (2025/12/12)** 
* Added repeat papers for 2023/24 and 2024/25. I want to add older papers, might get to this early next week.
* Added a visualisation page showing breakdown of marks by topic.

**0.1 (2025/12/03)** 
* Initial version with warts and all
* Only has final exam papers for 2022/23 --- 2024/25 (no repeats yet)

**TODO**

* Add more past papers (and don't add 2025/26)
* Perform a sanity check on topics, on tasks, and on keywords. (will do this when I add more papers so that all are consistent.)   
* Add description/summary for each task.   
""")