# pylint: disable=(missing-module-docstring)

import ast
import streamlit as st

import duckdb
from click import option
from duckdb.duckdb import query

con = duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)

st.title(
    """
SQL SRS
Spaced Repetition System SQL parctice
"""
)
options = ["CROSS JOIN", "WINDOW FUNCTION"]
with st.sidebar:
    theme = st.selectbox(
        "what would you like to revise?",
        options,
        index=None,
        placeholder="Select a theme...",
    )
    st.write("You selected:", theme)
    exercise = con.execute(f"SELECT * FROM memory_state where theme like '{theme}'").df()
    st.dataframe(exercise)
    exercise_tables = exercise.loc[0, 'tables']
    for table in exercise_tables:
        st.write(f"table: {table}")
        df_table = con.execute(f"SELECT * FROM '{table}'").df()
        st.dataframe(df_table)

# st.markdown(
#     "Récupère le nom des plats et leur prix en utilisant "
#     "une jointure entre les tables `food` et `price`"
# )

sql_query = st.text_area(label="Entrez votre requete: ")

tab2, tab3 = st.tabs(["Tables","Solution"])

with tab2:
    if sql_query:
        st.write("Votre table:")
        user_answer_table = con.execute(sql_query).df()
        st.dataframe(user_answer_table)
with tab3:
    solution = exercise.loc[0, 'exercises_name']
    file_name = "answers/" + solution + "_solution.sql"
    with open(file_name, "r") as f:
        sql_solution = f.read()
    st.code(sql_solution, language="sql")
































# try:
#     sql_table = duckdb.query(sql_query).df()
#     st.dataframe(sql_table)
#     sql_table_sorted = (
#         sql_table.sort_index(axis=1)
#         .sort_values(by=list(sql_table.columns))
#         .reset_index(drop=True)
#     )
#     data_result_sorted = (
#         data_result.sort_index(axis=1)
#         .sort_values(by=list(data_result.columns))
#         .reset_index(drop=True)
#     )
#     if sql_table_sorted.equals(data_result_sorted):
#         st.success("Correct ! La réponse est bien.")
#     else:
#         st.error("C'est Faux.")
#
# except AttributeError as e:
#     st.warning("Please enter a SQL query.")
#
#
# tab1, tab2 = st.tabs(["Tables", "Solution"])
#
# with tab1:
#     st.write("table: food")
#     st.dataframe(food)
#     st.write("table: price")
#     st.dataframe(price)
#     st.write("table: expected")
#     st.dataframe(data_result)
# with tab2:
#     st.write("Réponse:")
#     st.code(SQL_RESULT, language="sql")
#     st.dataframe(data_result)
