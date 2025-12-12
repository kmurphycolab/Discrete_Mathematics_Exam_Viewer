task_info = {}

# Construct a truth table.

task_info['Construct a truth table.'] = {
    'summary': """To construct a truth table you ...
* Identify the variables in in the proposition.
* The number of rows in the table is 2 the power of the number of variables.
* Generate the sequence of different inputs values.
* Parse the logical expression, each intermediate expression is a column in the table.
* Populate table cells with `False`/`True` values.
* Values in output column can be used to classify the proposition.
""",
    'related': ['Classify a logical proposition.']
}

# Classify a logical proposition.

task_info['Classify a logical proposition.'] = {
    'summary': """
Given a logical proposition determine if its truth value is 
* always `True` -> a **tautology**
* `True` for at least one input-> **satisfiable**
* never `True` -> a **contradiction**

Discrete_Mathematics_Exam_Viewer

To do this we usually first construct a truth table, then check the output column. 
""",
    'related': ['Construct a truth table.']
}

