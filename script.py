import streamlit as st
import pandas as pd
import duckdb
from io import StringIO
data_food = """food_id,food_name
1,Pizza
2,Burger
3,Sushi
4,Pasta
5,Salad
"""

# Données Price en format CSV
data_price = """food_id,price
1,8.99
2,5.49
3,12.99
4,7.50
6,4.99
"""

food = pd.read_csv(StringIO(data_food))
price = pd.read_csv(StringIO(data_price))

st.title("""
SQL SRS
Spaced Repetition System SQL parctice
""")
sql_result = """
        SELECT f.food_id, f.food_name, p.price
        FROM food f
        INNER JOIN price p ON f.food_id = p.food_id

"""
data_result = duckdb.query(sql_result).df()
with st.sidebar:
    option = st.selectbox(
        "what would you like to revise?",
        ["JOIN","GROUP BY","WINDOWS FUNCTIONS"],
        index =0,
        placeholder="Select a theme..."

    )
    st.write('You selected:', option)


st.write("enter your code:")
sql_query = st.text_area(label="Entrez votre requete: ")
sql_table = duckdb.query(sql_query).df()
st.dataframe(sql_table)
if sql_table.equals(data_result):
    st.success("Correct ! La réponse est bien.")
else:
    st.error("C'est Faux.")



tab1, tab2= st.tabs(["Tables", "Solution"])

with tab1:
    st.write("table: food")
    st.dataframe(food)
    st.write("table: price")
    st.dataframe(price)
    st.write("table: expected")
    st.dataframe(data_result)
with tab2:
    st.write("Réponse:")
    st.code(sql_result,language='sql')
    st.dataframe(data_result)

