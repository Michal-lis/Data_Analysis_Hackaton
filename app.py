import src.db.dataService as db
import src.db.preprocess as preprocess
import pandas


def main():
    connection = db.create_connection()

    result = db.get_columns_from_neighbouring_grids_near_stations(column="dochod_bud_pra",
                                                                  table_name="grid250_dochod",
                                                                  connection=connection,
                                                                  stations=stations,
                                                                  grid_count=9)
    averaged_results = preprocess.get_averages_per_station(result)
    print(averaged_results)


if __name__ == "__main__":
    main()
