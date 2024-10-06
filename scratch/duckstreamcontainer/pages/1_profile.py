import duckdb
import streamlit as st

con = duckdb.connect(database="./data/cheese.duckdb", read_only=True)

st.write("# Profile")

st.write("## Schema")

st.table(duckdb.sql("DESCRIBE SELECT * FROM cheeses;").df())

st.write("## Sample Data")

st.table(duckdb.sql("SELECT * FROM cheeses LIMIT 5;").df())
