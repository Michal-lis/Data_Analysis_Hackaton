import pandas as pd
import gmplot
import numpy as np
import matplotlib.pyplot as plotter
import data_science as ds
from pylab import cm
import matplotlib

def print_polygon_colored(gmap, pol_list,color):
    data_y, data_x = zip(*pol_list)
    # Polygon
    gmap.polygon(data_x, data_y, str(color), edge_width=0, filled=True)

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
    # gmap = gmplot.GoogleMapPlotter(52, 17, 50)
    # for x in coor:
    #     gmap.scatter([x[0]], [x[1]], 'cornflowerblue', edge_width=5, marker=False)
    #     gmap.draw("test.html")
    return coor, lat_range/grid_lat, lon_range/grid_lon

def make_square(center, width, height):
    poly = []
    poly.append([center[1] - height / 2, center[0] - width / 2])
    poly.append([center[1] - height / 2, center[0] + width / 2])
    poly.append([center[1] + height / 2, center[0] + width / 2])
    poly.append([center[1] + height / 2, center[0] - width / 2])
    return poly

def print_all_colored(gmap, coordinates):
    pass

if __name__ == "__main__":
    sensor_csv = "..\\..\\air-quality-data-from-extensive-network-of-sensors\sensor_locations.csv"
    coordinates, width, height = make_test_grid(sensor_csv, 10, 10)
    #print(coordinates)

    cmap = cm.get_cmap('rainbow', len(coordinates))
    gradient_list = []
    for i in range(cmap.N):
        rgb = cmap(i)[:3]  # will return rgba, we take only first 3 so we get rgb
        gradient_list.append(matplotlib.colors.rgb2hex(rgb))

    out = "..\\..\\out.csv"
    coordinates_2 = pd.read_csv(out)
    coordinates_2 = coordinates_2[['latitude', 'longitude', 'pm25']].values.tolist()
    coordinates_2.sort(key=lambda x: x[2])
    # out = "..\\..\\processed_data.csv"
    # coordinates_2 = pd.read_csv(out)
    # print(coordinates_2)
    # coordinates_2 = coordinates_2[['latitude', 'longitude', 'pm25']].values.tolist()
    # coordinates_2.sort(key=lambda x: x[2])

    cmap = cm.get_cmap('OrRd', len(coordinates_2))
    gradient_list = []
    for i in range(cmap.N):
        rgb = cmap(i)[:3]  # will return rgba, we take only first 3 so we get rgb
        gradient_list.append(matplotlib.colors.rgb2hex(rgb))

    for i in range(len(coordinates_2)):
       coordinates_2[i].append(gradient_list[i])

    gmap = gmplot.GoogleMapPlotter(50, 19, 50)
    for coor in coordinates_2:
        square = make_square(coor, width, height)
        print_polygon_colored(gmap, square, coor[3])
    gmap.draw("test_8.html")
