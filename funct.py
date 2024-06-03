import json
import psycopg2
from psycopg2 import sql


def process_json(file_paths):
    # Function to process a single JSON file
    def process_file(file_path):
        with open(file_path, "r") as f:
            data = json.load(f)
            extr_data = {}
            extr_data.update(data["value"])
            # Convert keys to integers and initialize the result dictionary
            result_dict = {i: None for i in range(30)}
            for key, value in extr_data.items():
                int_key = int(key)
                result_dict[int_key] = value
        return result_dict

    # Process each file and store the results in a list
    result_dicts = [process_file(file_path) for file_path in file_paths]
    return result_dicts


def insert_data_to_db(table_name, columns, data, conn):
    insert_query = (
        f"INSERT INTO {table_name} ({columns[0]}, {columns[1]}) VALUES (%s, %s)"
    )

    with conn.cursor() as cursor:
        for key, value in data.items():
            cursor.execute(insert_query, (key, value))
        conn.commit()


def main():
    file_paths = [
        "json_data/data_1.json",
        "json_data/data_2.json",
        "json_data/data_3.json",
    ]
    results = process_json(file_paths)

    conn_params = {
        "host": "localhost",
        "database": "postgres",
        "user": "postgres",
        "password": "123",
    }

    conn = psycopg2.connect(**conn_params)

    try:
        table_names_and_columns = [
            ("unemployment", ("id", "unemployment")),
            ("vacancy", ("id", "vacant")),
            ("population", ("id", "population")),
        ]
        for i, result in enumerate(results):
            table_name, columns = table_names_and_columns[i]
            insert_data_to_db(table_name, columns, result, conn)
            print(f"Inserted data from file {i+1} into {table_name}")
    finally:
        conn.close()


if __name__ == "__main__":
    main()
