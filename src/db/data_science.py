import psycopg2
import pprint
import gmplot
import pandas as pd

def plot_sensor_location(in_dir, out_dir, width=5):
    gmap = gmplot.GoogleMapPlotter(50, 19, 50)
    data = pd.read_csv(in_dir)
    # Polygon
    for row in data.iterrows():
        N = row[1][2]
        E = row[1][1]
        print(E,N)
        gmap.scatter([E], [N], 'cornflowerblue', edge_width=width, marker=False)
    gmap.draw(out_dir)

def plot_sensor_location(in_dir, out_dir, width=5):
    gmap = gmplot.GoogleMapPlotter(50, 19, 50)
    data = pd.read_csv(in_dir)
    # Polygon
    for row in data.iterrows():
        N = row[1][2]
        E = row[1][1]
        print(E,N)
        gmap.scatter([E], [N], 'cornflowerblue', edge_width=width, marker=False)
    gmap.draw(out_dir)

def connect_db():
    conn_string = "host='85.194.245.31' dbname='locit_sample' user='sample_user' password='!TajemniczaTajemnica7'"

    # print the connection string we will use to connect
    print(conn_string)

    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    cursor = conn.cursor()
    print("Connected!\n")
    return conn

def disconnect_db(conn):
    conn.close()

def from_eurogrid_to_coor(conn,eurogrid):
    querry = "SELECT ST_AsText(ST_Transform(geometria92,4674)) FROM locit_datasets.grid250 WHERE eurogrid_0250 IN ('" + str(eurogrid) + "')"
    out = get_sql(conn, querry)
    return out

def get_sql(conn, querry):
    cursor = conn.cursor()
    cursor.execute(querry)
    records = cursor.fetchall()
    return records

def plot_sensor_location(in_dir, out_dir, width=5):
    gmap = gmplot.GoogleMapPlotter(50, 19, 50)
    data = pd.read_csv(in_dir)
    # Polygon
    for row in data.iterrows():
        N = row[1][2]
        E = row[1][1]
        print(E,N)
        gmap.scatter([E], [N], 'cornflowerblue', edge_width=width, marker=False)
    gmap.draw(out_dir)

if __name__ == "__main__":
    #plot_sensor_location("sensor_locations.csv", "test.html")
    #plot_sensor_location("sensor_locations.csv", "test.html")
    conn = connect_db()
    #querry = "SELECT ST_AsText(geometria92) FROM locit_datasets.grid250 WHERE ST_Within(ST_SetSRID(ST_MakePoint(19.96, 50.05748),4674), ST_TRANSFORM(geometria92,4674))"
    #records = get_sql(conn, querry)
    #print(records)
    coor = from_eurogrid_to_coor(conn, '1kmN3278E4798_42')
    print(coor[0])
    disconnect_db(conn)