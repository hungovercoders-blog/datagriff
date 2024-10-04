import os

import duckdb
from IPython.display import display

# !! Remember need to add self explicitly to the lake as storage blob data contributor!!
duckdb.sql(
    """CREATE SECRET cheese (TYPE AZURE, PROVIDER CREDENTIAL_CHAIN, SCOPE 'abfss://lrndlkcheese12345hngc.dfs.core.windows.net/');"""
)

duckdb.sql(
    """
SET azure_transport_option_type = 'curl';
SET azure_http_stats = false;
SET azure_read_transfer_concurrency = 5;
SET azure_read_transfer_chunk_size = 1_048_576;
SET azure_read_buffer_size = 1_048_576;
"""
)  ## important for when running in linux!

duckdb.sql("""SELECT 'Bring me cheese!'""").show()

df_cheese = duckdb.sql(
    """
SELECT *
FROM 'abfss://lrndlkcheese12345hngc.dfs.core.windows.net/lake/csv/cheeses.csv'
"""
).df()

display(df_cheese.head(5))

df_cheese_described = duckdb.sql(
    """
DESCRIBE
FROM 'abfss://lrndlkcheese12345hngc.dfs.core.windows.net/lake/csv/cheeses.csv'
"""
).df()

display(df_cheese_described)

# df_wine = duckdb.sql(
#     """
# SELECT coalesce(Region,'(Unknown)') AS Region, count(*) AS Wines
# FROM 'abfss://lrndlkcheese1e269a0387.dfs.core.windows.net/lake/csv/cheeses.csv'
# GROUP BY ALL
# ORDER BY 2 DESC
# LIMIT 10
# """
# ).show()

# duckdb.sql("""SELECT 'Bring me wine!'""").show()

# df_wine = duckdb.sql(
#     """
# SELECT *
# FROM 'abfss://lrndlkwinee4769a04a5.dfs.core.windows.net/lake/csv/WineDataset.csv'
# """
# ).df()

# display(df_wine.head(5))

# display(list(df_wine.columns))

# df_wine = duckdb.sql(
#     """
# SELECT coalesce(Region,'(Unknown)') AS Region, count(*) AS Wines
# FROM 'abfss://lrndlkwinee4769a04a5.dfs.core.windows.net/lake/csv/WineDataset.csv'
# GROUP BY ALL
# ORDER BY 2 DESC
# LIMIT 10
# """
# ).show()
