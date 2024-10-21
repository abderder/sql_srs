# pylint: disable=(missing-module-docstring)


import streamlit as st

import duckdb

con = duckdb.connect(database="data/exercises_sql_tables.duckdb", read_only=False)

st.title(
    """
SQL SRS
Spaced Repetition System SQL parctice
"""
)

# SQL_RESULT = """
# SELECT f.food_id, f.food_name, p.price
# FROM food f
# INNER JOIN price p ON f.food_id = p.food_id
#
# """
# data_result = duckdb.query(SQL_RESULT).df()
with st.sidebar:
    theme = st.selectbox(
        "what would you like to revise?",
        ["CROSS JOIN", "GROUP BY", "WINDOW FUNCTION"],
        index=0,
        placeholder="Select a theme...",
    )
    st.write("You selected:", theme)
    exercise = con.execute(f"SELECT * FROM memory_state where theme like '{theme}'").df()
    st.dataframe(exercise)
#   st.
# st.markdown(
#     "Récupère le nom des plats et leur prix en utilisant "
#     "une jointure entre les tables `food` et `price`"
# )
#
# sql_query = st.text_area(label="Entrez votre requete: ")
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
