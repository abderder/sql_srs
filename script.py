import streamlit as st
import pandas as pd
import duckdb
from rich.jupyter import display

st.write("Hello world!")

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

data = {
    'Nom': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'Ville': ['Paris', 'Lyon', 'Marseille']
}
df = pd.DataFrame(data)
with tab1:
    st.write("Hello world! am tab1")
    sql_query = st.text_area(label="Entrez votre requete: ")
    result = duckdb.query(sql_query).df()
    st.write(f"vous aves entré la requéte suivante : ")
    st.code(sql_query, language='sql')

    st.dataframe(result)



with tab2:
    st.write("Hello world! am tab2")
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
    st.write("Hello world! am tab3")
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
