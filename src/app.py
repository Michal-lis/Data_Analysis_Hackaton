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
    sensors_data["income_9"] = pd.Series(averaged_results, index=sensors_data.index)

    result = db.get_columns_from_neighbouring_grids_near_stations(column="dochod_bud_pra",
                                                                  table_name="grid250_dochod",
                                                                  connection=connection,
                                                                  stations=[[row[1]['longitude'], row[1]['latitude']]
                                                                            for row
                                                                            in sensors_data.iterrows()],
                                                                  grid_count=16)
    averaged_results = preprocess.get_averages_per_station(result)
    sensors_data["income_16"] = pd.Series(averaged_results, index=sensors_data.index)

    result = db.get_columns_from_neighbouring_grids_near_stations(column="dochod_bud_pra",
                                                                  table_name="grid250_dochod",
                                                                  connection=connection,
                                                                  stations=[[row[1]['longitude'], row[1]['latitude']]
                                                                            for row
                                                                            in sensors_data.iterrows()],
                                                                  grid_count=25)
    averaged_results = preprocess.get_averages_per_station(result)
    sensors_data["income_25"] = pd.Series(averaged_results, index=sensors_data.index)

    population = db.get_columns_from_neighbouring_grids_near_stations(column="populacja_razem",
                                                                      table_name="grid250_demo_ext",
                                                                      connection=connection,
                                                                      stations=[
                                                                          [row[1]['longitude'], row[1]['latitude']]
                                                                          for row
                                                                          in sensors_data.iterrows()],
                                                                      grid_count=9)
    summed_population = preprocess.get_sum_per_station(population)

    sensors_data["populacja_9"] = pd.Series(summed_population, index=sensors_data.index)

    population = db.get_columns_from_neighbouring_grids_near_stations(column="populacja_razem",
                                                                      table_name="grid250_demo_ext",
                                                                      connection=connection,
                                                                      stations=[
                                                                          [row[1]['longitude'], row[1]['latitude']]
                                                                          for row
                                                                          in sensors_data.iterrows()],
                                                                      grid_count=16)
    summed_population = preprocess.get_sum_per_station(population)

    sensors_data["populacja_16"] = pd.Series(summed_population, index=sensors_data.index)

    population = db.get_columns_from_neighbouring_grids_near_stations(column="populacja_razem",
                                                                      table_name="grid250_demo_ext",
                                                                      connection=connection,
                                                                      stations=[
                                                                          [row[1]['longitude'], row[1]['latitude']]
                                                                          for row
                                                                          in sensors_data.iterrows()],
                                                                      grid_count=25)
    summed_population = preprocess.get_sum_per_station(population)

    sensors_data["populacja_25"] = pd.Series(summed_population, index=sensors_data.index)

    population = db.get_columns_from_neighbouring_grids_near_stations(column="budynki_all",
                                                                      table_name="grid250_demo_ext",
                                                                      connection=connection,
                                                                      stations=[
                                                                          [row[1]['longitude'], row[1]['latitude']]
                                                                          for row
                                                                          in sensors_data.iterrows()],
                                                                      grid_count=9)
    summed_population = preprocess.get_sum_per_station(population)

    sensors_data["budynki_all_9"] = pd.Series(summed_population, index=sensors_data.index)
    population = db.get_columns_from_neighbouring_grids_near_stations(column="budynki_all",
                                                                      table_name="grid250_demo_ext",
                                                                      connection=connection,
                                                                      stations=[
                                                                          [row[1]['longitude'], row[1]['latitude']]
                                                                          for row
                                                                          in sensors_data.iterrows()],
                                                                      grid_count=16)
    summed_population = preprocess.get_sum_per_station(population)

    sensors_data["budynki_all_16"] = pd.Series(summed_population, index=sensors_data.index)
    population = db.get_columns_from_neighbouring_grids_near_stations(column="budynki_all",
                                                                      table_name="grid250_demo_ext",
                                                                      connection=connection,
                                                                      stations=[
                                                                          [row[1]['longitude'], row[1]['latitude']]
                                                                          for row
                                                                          in sensors_data.iterrows()],
                                                                      grid_count=25)
    summed_population = preprocess.get_sum_per_station(population)

    sensors_data["budynki_all_25"] = pd.Series(summed_population, index=sensors_data.index)

    buildings = db.get_columns_from_neighbouring_grids_near_stations(column="budynki_mieszkalne",
                                                                     table_name="grid250_demo_ext",
                                                                     connection=connection,
                                                                     stations=[
                                                                         [row[1]['longitude'], row[1]['latitude']]
                                                                         for row
                                                                         in sensors_data.iterrows()],
                                                                     grid_count=9)
    summed_population = preprocess.get_sum_per_station(buildings)

    sensors_data["budynki_mieszkalne_9"] = pd.Series(summed_population, index=sensors_data.index)

    buildings = db.get_columns_from_neighbouring_grids_near_stations(column="budynki_mieszkalne",
                                                                     table_name="grid250_demo_ext",
                                                                     connection=connection,
                                                                     stations=[
                                                                         [row[1]['longitude'], row[1]['latitude']]
                                                                         for row
                                                                         in sensors_data.iterrows()],
                                                                     grid_count=16)
    summed_population = preprocess.get_sum_per_station(buildings)

    sensors_data["budynki_mieszkalne_16"] = pd.Series(summed_population, index=sensors_data.index)
    buildings = db.get_columns_from_neighbouring_grids_near_stations(column="budynki_mieszkalne",
                                                                     table_name="grid250_demo_ext",
                                                                     connection=connection,
                                                                     stations=[
                                                                         [row[1]['longitude'], row[1]['latitude']]
                                                                         for row
                                                                         in sensors_data.iterrows()],
                                                                     grid_count=25)
    summed_population = preprocess.get_sum_per_station(buildings)

    sensors_data["budynki_mieszkalne_25"] = pd.Series(summed_population, index=sensors_data.index)


if __name__ == "__main__":
    main()
