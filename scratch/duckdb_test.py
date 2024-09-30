import duckdb
from IPython.display import display

duckdb.sql(
    """SET azure_transport_option_type = 'curl'"""
)  ## important for when running in linux!

duckdb.sql("""SELECT 'Bring me cheese!'""").show()

df_cheese = duckdb.sql(
    """
SELECT *
FROM 'abfss://lrndlkcheese1e269a0387.dfs.core.windows.net/lake/csv/cheeses.csv'
"""
).df()

display(df_cheese.head(5))

display(list(df_cheese.columns))

df_wine = duckdb.sql(
    """
SELECT coalesce(Region,'(Unknown)') AS Region, count(*) AS Wines
FROM 'abfss://lrndlkcheese1e269a0387.dfs.core.windows.net/lake/csv/cheeses.csv'
GROUP BY ALL
ORDER BY 2 DESC
LIMIT 10
"""
).show()

duckdb.sql("""SELECT 'Bring me wine!'""").show()

df_wine = duckdb.sql(
    """
SELECT *
FROM 'abfss://lrndlkwinee4769a04a5.dfs.core.windows.net/lake/csv/WineDataset.csv'
"""
).df()

display(df_wine.head(5))

display(list(df_wine.columns))

df_wine = duckdb.sql(
    """
SELECT coalesce(Region,'(Unknown)') AS Region, count(*) AS Wines
FROM 'abfss://lrndlkwinee4769a04a5.dfs.core.windows.net/lake/csv/WineDataset.csv'
GROUP BY ALL
ORDER BY 2 DESC
LIMIT 10
"""
).show()
