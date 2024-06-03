import json

ind = {}
lab = {}
extr_data = {}

with open("json_data/data_1.json", "r") as f:
    data = json.load(f)
    ind.update(data["dimension"]["geo"]["category"]["index"])
    lab.update(data["dimension"]["geo"]["category"]["label"])

extr_data["id"] = list(ind.values())
extr_data["code"] = list(ind.keys())
extr_data["country"] = list(lab.values())

import psycopg2

conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=123")
cur = conn.cursor()
cur.execute(
    """
    CREATE TABLE core(
	    id int PRIMARY KEY,
	    code varchar(10),
	    country varchar(30)
    )
    """
)
cur.execute(
    """
    CREATE TABLE unemployment(
	    id int,
	    unemployment int
    )
    """
)
cur.execute(
    """
    CREATE TABLE vacancy(
	    id int,
	    vacant int
    )
    """
)
cur.execute(
    """
    CREATE TABLE population(
	id int,
	population int
    )
    """
)
conn.commit()

insert_query = "INSERT INTO core (id, code, country) VALUES (%s, %s, %s)"

for i in range(len(extr_data["id"])):
    cur.execute(
        insert_query,
        (extr_data["id"][i], extr_data["code"][i], extr_data["country"][i]),
    )

# Commit the transaction
conn.commit()
