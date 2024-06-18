Pipeline is divided into 3 files in the order:
  1. get_json - takes data from the sources
  2. create_tables - connects to Postgres and creates 4 tables: core with ids and countries, unemployment, vacancy and population
  3. funct - parses json files and injects data into corresponding tables.
