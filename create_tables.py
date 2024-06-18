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
