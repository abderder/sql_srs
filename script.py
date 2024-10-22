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


solution = exercise.loc[0, 'exercises_name']
file_name = "answers/" + solution + "_solution.sql"
with open(file_name, "r") as f:
    sql_solution = f.read()
answer_table = con.execute(sql_solution).df()

sql_query = st.text_area(label="Entrez votre requete: ")

tab2, tab3 = st.tabs(["Tables","Solution"])

with tab2:
    #Utilisateur réponse
    if sql_query:
        st.write("Votre table:")
        try:
            user_answer_table = con.execute(sql_query).df()
            st.dataframe(user_answer_table)
        except Exception as e:
            error_message = str(e)
            st.error(error_message)
        try:
            user_answer_table_sorted = (
                user_answer_table.sort_index(axis=1)
                .sort_values(by=user_answer_table.columns[1])
                .reset_index(drop=True)
            )
            answer_table_sorted = (
                answer_table.sort_index(axis=1)
                .sort_values(by=answer_table.columns[1])
                .reset_index(drop=True)
            )
            if user_answer_table_sorted.equals(answer_table_sorted):
                st.success("Correct ! La réponse est bien.")
            else:
                st.error("C'est Faux.")
        except Exception as e:
            st.error("Please enter a SQL query.")
with tab3:
    st.code(sql_solution, language="sql")












# st.markdown(
#     "Récupère le nom des plats et leur prix en utilisant "
#     "une jointure entre les tables `food` et `price`"
# )
















