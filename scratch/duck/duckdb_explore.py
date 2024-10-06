import duckdb
from IPython.display import display

print("""Set storage account path variables.""")
storage_account_name = "lrndlkcheese12345hngc"
storage_account_url = (
    "abfss://{}.dfs.core.windows.net".format(storage_account_name) + "/"
)
directory_cheese = "lake/csv/cheeses.csv"
cheese_path = "{}{}".format(storage_account_url, directory_cheese)

print("""Update any duckdb extensions""")
duckdb.sql("update extensions").show()

print(
    """Create cheese secret to access storage. !!Remember to az login and ensure your account has storage blob data contributor on the container!!"""
)
duckdb.sql(
    f"""CREATE SECRET cheese (TYPE AZURE, PROVIDER CREDENTIAL_CHAIN, SCOPE '{storage_account_url}');"""
)
print("""Show secrets currently available in duckdb.""")
duckdb.sql("FROM duckdb_secrets();").show()
print("""Show secret that will be used for the storage you are going to access.""")
duckdb.sql(f"FROM which_secret('{storage_account_url}', 'azure');").show()

print(
    """Set recommended configuration options for accessing Azure. Note curl transport option type is currently needed for linux."""
)
duckdb.sql(
    """
SET azure_transport_option_type = 'curl'; --important for when running in linux!
SET azure_http_stats = false;
SET azure_read_transfer_concurrency = 5;
SET azure_read_transfer_chunk_size = 1_048_576;
SET azure_read_buffer_size = 1_048_576;
"""
)

print("""Confirm a simple select statement.""")
duckdb.sql("""SELECT 'Bring me cheese!'""").show()

print("""Describe cheese data""")
df_cheese_described = duckdb.sql(
    f"""
DESCRIBE
FROM '{cheese_path}'
"""
).df()

print("""Display described cheese data""")
display(df_cheese_described)

print("""Create cheese dataframe""")
df_cheese = duckdb.sql(
    # TODO: how to prevent sql injection
    # trunk-ignore(bandit/B608)
    f"""
SELECT *
FROM '{cheese_path}'
"""
).df()

print("""Display top 5 cheese data""")
display(df_cheese.head(5))
