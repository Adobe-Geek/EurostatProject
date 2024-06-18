import psycopg2
import time


def connect_to_postgres():
    host = "localhost"
    database = "postgres"
    user = "postgres"
    password = "123"

    attempt = 0
    max_attempts = 10
    interval = 60  # 1 minute

    while attempt < max_attempts:
        try:
            connection = psycopg2.connect(
                host=host, database=database, user=user, password=password
            )
            print("Connection successful")
            return connection
        except psycopg2.OperationalError as e:
            attempt += 1
            print(f"Attempt {attempt} failed: {e}")
            if attempt < max_attempts:
                print(f"Retrying in {interval} seconds...")
                time.sleep(interval)

    print("Server is down")
    return None


if __name__ == "__main__":
    conn = connect_to_postgres()

    if conn:
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
        cur.close()
        conn.close()
