import pandas as pd
import gmplot

def make_test_grid(sensor_input, grid_lat, grid_lon):
    data_sensors = pd.read_csv(sensor_input)
    coor_max = [data_sensors['latitude'].max(), data_sensors['longitude'].max()]
    coor_min = [data_sensors['latitude'].min(), data_sensors['longitude'].min()]

    lat_range = coor_max[0] - coor_min[0]
    lon_range = coor_max[1] - coor_min[1]
    coor = []
    for iter_lat in range(grid_lat):
        for iter_lon in range(grid_lon):
            coor.append([coor_min[0] + iter_lat * lat_range / grid_lat, coor_min[1] + iter_lon * lon_range / grid_lon])
    gmap = gmplot.GoogleMapPlotter.from_geocode("Krakow")
    #for x in coor:
    #   gmap.scatter([x[0]], [x[1]], 'cornflowerblue', edge_width=5, marker=False)
    #   gmap.draw("test.html")
    return coor

if __name__ == "__main__":
    sensor_csv = "..\\..\\air-quality-data-from-extensive-network-of-sensors\sensor_locations.csv"
    coordinates = make_test_grid(sensor_csv, 4, 5)
    print(coordinates)