import src.db.dataService as db
import src.db.preprocess as preprocess


def main():
    connection = db.create_connection()
    stations = [[20, 50], [20, 50.1]]
    result = db.get_columns_from_neighbouring_grids_near_stations(column="dochod_bud_pra",
                                                                  table_name="grid250_dochod",
                                                                  connection=connection,
                                                                  stations=stations,
                                                                  grid_count=9)
    averaged_results = preprocess.get_averages_per_station(result)
    print(averaged_results)


if __name__ == "__main__":
    main()
