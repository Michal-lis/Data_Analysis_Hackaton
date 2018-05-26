import src.db.dataService as db


def main():
    connection = db.create_connection()
    # print(db.get_all_from_table("poi", connection))
    print(db.get_columns_from_table(table_name="poi",
                                    columns=["poi_category_name", "poi_subcategory_name"],
                                    connection=connection))


if __name__ == "__main__":
    main()
