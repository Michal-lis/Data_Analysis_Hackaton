import src.db.dataService as db
import src.db.preprocess as preprocess
import pandas as pd

from src.tools import free_open_elevation


def get_location_features_by_squares(sensors_data, conn, features, squares):
    for table, feature in features:
        for no_squares in squares:
            result = db.get_columns_from_neighbouring_grids_near_stations(column=feature,
                                                                          table_name=table,
                                                                          connection=conn,
                                                                          stations=[
                                                                              [row[1]['longitude'], row[1]['latitude']]
                                                                              for row
                                                                              in sensors_data.iterrows()],
                                                                          grid_count=no_squares)
            summed_results = preprocess.get_sum_per_station(result)
            sensors_data["{}_{}".format(feature, no_squares)] = pd.Series(summed_results, index=sensors_data.index)
    return sensors_data


def get_location_features_by_radius(sensors_data, conn, features_config):
    for feature, radiuses in features_config.items():
        for radius in radiuses:
            sensors_data["{}_{}".format(feature, radius)] = [
                db.get_no_places_in_radius(row['longitude'], row['latitude'], radius, feature, conn)
                for id, row in sensors_data.iterrows()]
    return sensors_data


def get_elevation_data(sensors_data):
    sensors_data['elevation'] = [free_open_elevation(row['latitude'], row['longitude']) for id, row in
                                 sensors_data.iterrows()]
    return sensors_data

def get_all_features(data, conn):
    features_by_squares = [
        ('grid250_dochod', 'dochod_bud_pra'),
        ('grid250_demo_ext', 'populacja_razem'),
        ('grid250_demo_ext', 'budynki_all'),
        ('grid250_demo_ext', 'budynki_mieszkalne'),
    ]
    squares = [9, 16, 25]

    features_by_radius = {
        'Przystanek autobusowy': [1000, 2000],
        'Oddział Banku': [1000, 2000],
        'Przystanek tramwajowy': [1000, 2000],
        'Hipermarket': [1000, 2000],
        'Stacja Paliw': [1000, 3000]
    }

    data = get_location_features_by_squares(data, conn, features_by_squares, squares)
    data = get_location_features_by_radius(data, conn, features_by_radius)
    data = get_elevation_data(data)
    return data
