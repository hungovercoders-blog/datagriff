import duckdb
import plotly.express as px
import streamlit as st

st.write("# Dashboard")

st.write("## Top Ten Cheeses by Region")


@st.cache_data
def load_region_data():
    df = duckdb.sql(
        """SELECT region, count(*) AS cheeses FROM cheeses
                        WHERE region <> 'NA'
                        GROUP BY region
                        ORDER BY cheeses DESC
                        LIMIT 10"""
    ).df()
    return df


st.bar_chart(load_region_data(), x="region", y="cheeses")

st.write("## Countries with the Biggest Cheese Slice")


@st.cache_data
def load_country_data():
    df = duckdb.sql(
        """WITH CTE AS (SELECT country, count(*) AS cheeses FROM cheeses
                        WHERE region <> 'NA'
                        GROUP BY country)
                        SELECT CASE WHEN cheeses > 1 THEN country ELSE 'Other' END AS country, sum(cheeses) as cheeses FROM CTE GROUP BY all
                        """
    ).df()
    return df


# Create a pie chart using Plotly
fig = px.pie(
    load_country_data(),
    values="cheeses",
    names="country",
    title="Countries with the Biggest Cheese Slice",
)

# Display the pie chart in the Streamlit app
st.plotly_chart(fig)
