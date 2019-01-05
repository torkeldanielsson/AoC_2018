import sys
import copy
from datetime import datetime
import operator

f = open("input.txt", "r")
lines = f.readlines()
f.close()

#132, 308

class Coord:
    x = 0
    y = 0

coords = []

for line in lines:
    parts = line.strip().split(", ")
    coord = Coord()
    coord.x = int(parts[1])
    coord.y = int(parts[0])
    coords.append(coord)

#for coord in coords:
#    print(coord.x, coord.y)

edge_len = 900

offset = 200

area = []

for i in range(edge_len):
    area.append([-1] * edge_len)

part_2_region = 0

for xi in range(0, edge_len):
    x = xi - offset
    for yi in range(0, edge_len):
        y = yi - offset

        best_dist = 1000000
        best_coord_index = -1
        double = False

        part_2_sum = 0

        for coord_index in range(0, len(coords)):
            coord = coords[coord_index]

            dist = abs(coord.x - x) + abs(coord.y - y)

            part_2_sum += dist

            if x == 1 and y == 5:
                print(double, coord_index, dist, best_dist, best_coord_index)

            if dist <= best_dist:
                if dist == best_dist:
                    double = True
                else:
                    double = False
                best_dist = dist
                best_coord_index = coord_index

            if x == 1 and y == 5:
                print(double, coord_index, dist, best_dist, best_coord_index)

        if double == False:
            area[xi][yi] = best_coord_index

        if part_2_sum < 10000:
            part_2_region += 1

#for x in range(0, edge_len):
#    line_string = ""
#    for y in range(len(area[x])):
#        d = area[x][y]
#        is_coord = False
#        for coord in coords:
#            if x == coord.x and y == coord.y:
#                is_coord = True
#        if is_coord:
#            line_string += str(chr(65 + d%25))
#        else:
#            line_string += "."
#    print(line_string)
#print("")

#for x in range(0, edge_len):
#    line_string = ""
#    for y in range(len(area[x])):
#        d = area[x][y]
#        if d == -1:
#            line_string += "."
#        else:
#            is_coord = False
#            for coord in coords:
#                if x == coord.x and y == coord.y:
#                    is_coord = True
#            if is_coord:
#                line_string += str(chr(65 + d%25))
#            else:
#                line_string += str(chr(97 + d%25))
#    print(line_string)
#print("")

class Result:
    coord_index = 0
    count = 0

results = []

for coord_index in range(0, len(coords)):
    count = 0
    for x in range(1, edge_len - 1):
        for y in range(1, edge_len - 1):
            if area[x][y] == coord_index:
                count += 1
    r = Result()
    r.coord_index = coord_index
    r.count = count
    results.append(r)

results.sort(key = operator.attrgetter('count'))

for res in results:
    coord = coords[res.coord_index]
    print("coord index: " + str(res.coord_index) + " [" + str(coord.x) + ", " + str(coord.y) + "] count:", res.count)

print("part 2 region size: ", part_2_region)