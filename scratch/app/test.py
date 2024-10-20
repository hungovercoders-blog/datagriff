import duckdb

con = duckdb.connect(database="./data/cheese.duckdb", read_only=False)

duckdb.sql("CREATE TABLE cheeses AS SELECT * FROM read_csv_auto('./data/cheeses.csv');")

duckdb.sql("SELECT * FROM cheeses LIMIT 5;").show()

duckdb.sql("DESCRIBE SELECT * FROM cheeses;").show()

duckdb.sql("SHOW TABLES;").show()
