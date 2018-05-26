import psycopg2


def create_connection():
    conn_string = "host='85.194.245.31' dbname='locit_sample' user='sample_user' password='!TajemniczaTajemnica7'"
    return psycopg2.connect(conn_string)


def get_all_from_table(table_name: str, connection):
    cursor = connection.cursor()
    print("Connected!\n")
    cursor.execute("SELECT * FROM locit_datasets." + table_name)
    return cursor.fetchall()
