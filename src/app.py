import src.db.dataService as db
import src.db.preprocess as preprocess
import pandas as pd

from get_location_features import get_location_features_by_squares, get_location_features_by_radius, get_elevation_data


def main():
    connection = db.create_connection()
    sensors_data = pd.read_csv(
        "data/air-quality-data-from-extensive-network-of-sensors/sensor_locations.csv").set_index(
        'id')
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

    sensors_data = get_location_features_by_squares(sensors_data, connection, features_by_squares, squares)
    sensors_data = get_location_features_by_radius(sensors_data, connection, features_by_radius)
    sensors_data = get_elevation_data(sensors_data)
    print(sensors_data.head())


if __name__ == "__main__":
    main()
