
search_by_keyword_intro = """

The **keywords** are a list of words/phrases  generated from the question text and the topic/task/concepts that they are based on.

To maximise finding of questions, there is some redundancy in the keywords (for example, "AP" and "arithmetic progression", or "injective" and "one-to-one").
However I (ironically, given my spelling) am using exact spelling, but to avoid issues with that you selected keywords from a multi-select list rather than typing them in. 
"""


search_by_task_intro = """
A **task** is a general process (sequence of steps) such as "_Construct a truth table._", etc. 
Most questions will consist of a single task, but some consist of two task. For example, 
a question could tasks "_Represent a relation as a digraph._" add "_Identify properties of a relation._".
"""

search_by_topic_intro = """
The Discrete Mathematics module is divided into topics, sub-topics and in some cases sub-sub-topics.
This division is follows closely the organisational structure of the notes.

Note that there is no topic "Computational Thinking" since that appears 
across all other topics in the python questions. 
So search by keyword "python" to find these questions.
"""

difficulty = {
    1:"direct application of definitions/notation covered in notes",
    2:"direct / straight forward computational task.",
    3:"computational task with some minor twists.",
    4:"more complicated problem / task.",
    5:"subtle or abstract question to stretch understanding of concepts.",
}

search_by_difficulty_intro = """
The **difficulty** is a very, very crude metric on how hard the question is.
The difficulty is an integer from 1 to 5 inclusive where:
""" + "\n".join([f"{k}. {v}" for k,v in difficulty.items()])

search_by_paper_intro = """
To be honest, I can't see why one would want to search questions by exam paper since an exam paper has the questions in the correct order anyway, but I was bored so added this page. 
""" 

grade_predictor_intro = """
This is a very crude and probably useless predictor of grades. 
Instead it should be called something like 
"_How much of the course have I mastered?_" but that title is too long.  
I did consider "_How F**ked am I?_" as the title, but stopped myself in time.

* For each task, give your level of competence. 
* Then a very crude simulation loops over each question in a past exam paper
  * Using the inputted skill levels and the question difficulty, estimate the marks awarded based on the task.
* Repeat simulation 100 times, because averaging will always make things more accurate? (no, it won't)

To be honest, this calculation is only a little better than an LLM. 
I have tried to tune it so that its predictions are reasonable but 
there is zero validation behind it.
"""
