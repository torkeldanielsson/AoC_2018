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
    coord.x = int(parts[0])
    coord.y = int(parts[1])
    coords.append(coord)

#for coord in coords:
#    print(coord.x, coord.y)

edge_len = 1000

offset = 250

area = []

for i in range(edge_len):
    area.append([-1] * edge_len)

for coord_index in range(0, len(coords)):
    coord = coords[coord_index]
    if coord.x + offset < edge_len and coord.y + offset < edge_len:
        area[coord.x + offset][coord.y + offset] = coord_index

#area[1][1] = 1
#area[5][5] = 2
#area[9][9] = 3

didChange = True

neighbors = [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]

class Change:
    x = 0
    y = 0
    coord_index = 0

while didChange:
    didChange = False

    change_list = []

    for x in range(1, edge_len - 1):
        for y in range(1, edge_len - 1):
            if area[x][y] == -1:
                coord_index = -1
                too_many_neighbors = False
                for n in neighbors:
                    if area[x + n[0]][y + n[1]] != -1:
                        if coord_index != -1 and area[x + n[0]][y + n[1]] != coord_index:
                            too_many_neighbors = True
                        coord_index = area[x + n[0]][y + n[1]]
                if coord_index != -1 and not too_many_neighbors:
                    didChange = True
                    change = Change()
                    change.x = x
                    change.y = y
                    change.coord_index = coord_index
                    change_list.append(copy.deepcopy(change))

    for change in change_list:
        area[change.x][change.y] = change.coord_index

#for i in range(0, edge_len):
#    line_string = ""
#    for d in area[i]:
#        if d == -1:
#            line_string += "."
#        else:
#            line_string += str(chr(33 + d%93))
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
