import duckdb
import streamlit as st

st.set_page_config(
    page_title="Cheese",
)

st.write("# Cheese")

con = duckdb.connect(database="./data/cheese.duckdb", read_only=False)

duckdb.sql(
    "CREATE TABLE IF NOT EXISTS cheeses AS SELECT * FROM read_csv_auto('./data/cheeses.csv');"
)
