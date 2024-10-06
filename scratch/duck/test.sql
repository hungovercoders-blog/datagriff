CREATE SECRET cheese (TYPE AZURE, 
PROVIDER CREDENTIAL_CHAIN
, SCOPE 'abfss://lrndlkcheese12345hngc.dfs.core.windows.net/')

SELECT *
FROM 'abfss://lrndlkcheese12345hngc.dfs.core.windows.net/lake/csv/cheeses.csv'