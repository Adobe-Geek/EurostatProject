create_tables - connects to Postgres and creates 4 tables: core with ids and countries, unemployment, vacancy and population

Pipeline itself is divided into 2 files in the order:
  1. get_json - takes data from the sources
  2. funct - parses json files and injects data into corresponding tables.
