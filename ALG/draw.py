import matplotlib.pyplot as plt
import numpy as np
import os
import sys

#工作环境变当前目录
current_path = os.path.dirname(__file__)




def read_coords_from_file(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    coords = []
    node_coord_section_found = False
    for line in lines:
        if line.startswith('NODE_COORD_SECTION'):
            node_coord_section_found = True
        elif node_coord_section_found:
            if line.startswith('EOF'):
                break
            node_id, x, y = line.strip().split()[0:3]
            coords.append((float(x), float(y)))
    return coords

def plot_points(coords):
    x_coords, y_coords = zip(*coords)
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(x_coords, y_coords, s=50, alpha=0.7)
    ax.set_xlabel('X Coordinate')
    ax.set_ylabel('Y Coordinate')
    ax.set_title('AME: TPS Dataset')
    plt.show()

def plot_best_route(file_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()
    route_coords = []
    tour_section_found = False
    for line in lines:
        if line.startswith('TOUR_SECTION'):
            tour_section_found = True
        elif tour_section_found:
            if line.startswith('-1'):
                break
            node_id = int(line.strip())
            x, y = coords[node_id - 1]
            route_coords.append((x, y))
    x,y=coords[0]
    route_coords.append((x,y))
    x_coords, y_coords = zip(*route_coords)
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(x_coords, y_coords, s=0.01, alpha=0.5, color='blue')
    #ax.plot(x_coords, y_coords, alpha=0.7, color='red')
    ax.plot(x_coords, y_coords, alpha=0.5, color='red')
    ax.set_xlabel('X Coordinate')
    ax.set_ylabel('Y Coordinate')
    ax.set_title('AME: TPS Best Route')
    plt.show()

# 读取数据集并绘制散点图
#coords = read_coords_from_file('D:\\CodeProgram\\python\\ALG\\berlin52.tsp')
coords = read_coords_from_file('D:\\CodeProgram\\python\\ALG\\scenery8_2w.tsp')

#plot_points(coords)

# 绘制最佳路径
#plot_best_route('D:\\CodeProgram\\python\\ALG\\berlinbest.tsp')
plot_best_route('D:\\CodeProgram\\python\\ALG\\secenery8_2w.tour')