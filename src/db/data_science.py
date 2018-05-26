import psycopg2
import pprint
import gmplot
import pandas as pd
import dataService as db
import preprocess as preprocess
import os


def print_polygon(gmap, pol_list):
    data_y, data_x = zip(*pol_list)
    # Polygon
    gmap.polygon(data_x, data_y, 'cornflowerblue', edge_width=5, filled=True)


def plot_sensor_location(in_dir, out_dir, width=10):
    gmap = gmplot.GoogleMapPlotter(50, 19, 50)
    data = pd.read_csv(in_dir)
    # Polygon
    for row in data.iterrows():
        N = row[1][2]
        E = row[1][1]
        print(E, N)
        gmap.scatter([E], [N], 'cornflowerblue', edge_width=width, marker=False)
    gmap.draw(out_dir)


def connect_db():
    conn_string = "host='85.194.245.31' dbname='locit_sample' user='sample_user' password='!TajemniczaTajemnica7'"
    print(conn_string)
    conn = psycopg2.connect(conn_string)
    cursor = conn.cursor()
    print("Connected!\n")
    return conn


def parser_for_euro(a):
    l = []
    for pair in a[0].split('(((')[1].split(')))')[0].split(','):
        a = float(pair.split(' ')[0])
        b = float(pair.split(' ')[1])
        l.append((a, b))
    return l


def disconnect_db(conn):
    conn.close()


def from_eurogrid_to_coor(conn, eurogrid):
    querry = "SELECT ST_AsText(ST_Transform(geometria92,4674)) FROM locit_datasets.grid250 WHERE eurogrid_0250 IN ('" + str(
        eurogrid) + "')"
    out = get_sql(conn, querry)
    out = parser_for_euro(out[0])
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
        print(E, N)
        gmap.scatter([E], [N], 'cornflowerblue', edge_width=width, marker=False)
    gmap.draw(out_dir)


def _build_query_grids(column: str, station, table_name: str, grid_count):
    query_template = """
SELECT xd.XD
FROM (
SELECT 	max(#TABLE#.#COLUMN#) as XD, #TABLE#.eurogrid_0250
                FROM	(
                    SELECT DISTINCT
                      grid250.eurogrid_0250,
                      ST_Distance_sphere(ST_SetSRID(ST_MakePoint(#LONGITUDE#, #LATITUDE#),4674), ST_Centroid(ST_TRANSFORM(geometria92,4674) )) as dist
                    FROM 
                      locit_datasets.grid250
                    ORDER BY dist
                    LIMIT #GRIDS#
                ) as lista_id_gridow
                INNER JOIN locit_datasets.#TABLE#
                ON (lista_id_gridow.eurogrid_0250 = #TABLE#.eurogrid_0250)
Group by #TABLE#.eurogrid_0250) as xd
"""

    query_template = query_template.replace("#TABLE#", table_name)
    query_template = query_template.replace("#COLUMN#", column)
    query_template = query_template.replace("#LONGITUDE#", str(station[0]))
    query_template = query_template.replace("#LATITUDE#", str(station[1]))
    query_template = query_template.replace("#GRIDS#", str(grid_count))
    return query_template


def get_columns_from_neighbouring_grids_near_stations(column: str, stations, table_name: str, connection, grid_count):
    results = []
    cursor = connection.cursor()
    for station in stations:
        query = _build_query_grids(column, station, table_name, grid_count)
        cursor.execute(query)
        results.append(cursor.fetchall())

    return results


if __name__ == "__main__":
    conn = connect_db()
    # test of a simple one eurogrid
    gmap2 = gmplot.GoogleMapPlotter(52, 17, 50)
    coor = from_eurogrid_to_coor(conn, '1kmN3042E5057_22')
    print_polygon(gmap2, coor)
    gmap2.draw("test_8.html")

    # test of all grids
    data_sensors = pd.read_csv(
        "Data_Analysis_Hackaton/air-quality-data-from-extensive-network-of-sensors/sensor_locations.csv")
    data_to_print = []
    for x in data_sensors.iterrows():
        data_to_print.append([x[1]['longitude'], x[1]['latitude']])
    print(data_to_print)
    result = db.get_columns_from_neighbouring_grids_near_stations(column="eurogrid_0250", table_name="grid250",
                                                                  connection=conn, stations=data_to_print,
                                                                  grid_count=9)
    gmap = gmplot.GoogleMapPlotter(52, 17, 50)
    print(result)
    for coord in result:
        print(coord)
        for coord2 in coord:
            print(coord2[0])
            eurogrid = coord2[0]
            coordinates = from_eurogrid_to_coor(conn, eurogrid)
            print_polygon(gmap, coordinates)
    gmap.draw("test_9.html")
    # print(coor)
    disconnect_db(conn)
