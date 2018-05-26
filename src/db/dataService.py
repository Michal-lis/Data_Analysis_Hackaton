import psycopg2


def create_connection():
    conn_string = "host='85.194.245.31' dbname='locit_sample' user='sample_user' password='!TajemniczaTajemnica7'"
    return psycopg2.connect(conn_string)


def get_all_from_table(table_name: str, connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM locit_datasets." + table_name)
    return cursor.fetchall()


def get_columns_from_table(table_name, columns, connection):
    cursor = connection.cursor()
    columns_string = columns[0]
    if len(columns) > 1:
        for col in columns:
            columns_string += ", " + col
    query = "SELECT " + columns_string + " FROM locit_datasets." + table_name
    cursor.execute(query)
    return cursor.fetchall()
