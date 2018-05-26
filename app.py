import src.db.dataService as db
import src.db.preprocess as preprocess
import pandas as pd


def main():
    connection = db.create_connection()
    sensors_data = pd.read_csv("air-quality-data-from-extensive-network-of-sensors/sensor_locations.csv").set_index(
        'id')

    result = db.get_columns_from_neighbouring_grids_near_stations(column="dochod_bud_pra",
                                                                  table_name="grid250_dochod",
                                                                  connection=connection,
                                                                  stations=[[row[1]['longitude'], row[1]['latitude']]
                                                                            for row
                                                                            in sensors_data.iterrows()],
                                                                  grid_count=9)
    averaged_results = preprocess.get_averages_per_station(result)
    sensors_data["income9"] = pd.Series(averaged_results, index=sensors_data.index)
    #
    # result = db.get_columns_from_neighbouring_grids_near_stations(column="dochod_bud_pra",
    #                                                               table_name="grid250_dochod",
    #                                                               connection=connection,
    #                                                               stations=[[row[1]['longitude'], row[1]['latitude']]
    #                                                                         for row
    #                                                                         in sensors_data.iterrows()],
    #                                                               grid_count=16)
    # averaged_results = preprocess.get_averages_per_station(result)
    # sensors_data["income16"] = pd.Series(averaged_results, index=sensors_data.index)
    #
    # result = db.get_columns_from_neighbouring_grids_near_stations(column="dochod_bud_pra",
    #                                                               table_name="grid250_dochod",
    #                                                               connection=connection,
    #                                                               stations=[[row[1]['longitude'], row[1]['latitude']]
    #                                                                         for row
    #                                                                         in sensors_data.iterrows()],
    #                                                               grid_count=25)
    # averaged_results = preprocess.get_averages_per_station(result)
    # sensors_data["income25"] = pd.Series(averaged_results, index=sensors_data.index)

    print(sensors_data)


if __name__ == "__main__":
    main()
