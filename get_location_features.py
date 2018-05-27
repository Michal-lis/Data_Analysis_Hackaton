import src.db.dataService as db
import src.db.preprocess as preprocess
import pandas as pd

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
