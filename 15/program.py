import sys
import copy
from datetime import datetime
import operator

f = open("test_1.txt", "r")
lines = f.readlines()
f.close()

def print_map(map, units):
    for y, row in enumerate(map):
        row_str = ""
        unit_str = " "
        for x, loc in enumerate(row):

            isUnit = False
            for unit in units:
                if unit.pos == (x, y):
                    isUnit = True
                    unit_desc = "G"
                    if unit.isElf:
                        unit_desc = "E"
                    row_str += unit_desc
                    unit_str += unit_desc + str(unit.hp) + ", "

            if not isUnit:
                if loc:
                    row_str += "#"
                else:
                    row_str += " "
        print(row_str + unit_str)

class Unit:
    isElf = True
    hp = 200
    ap = 3
    pos = (0, 0)

    def __lt__(self, other):
        if self.pos[1] == other.pos[1]:
            return self.pos[0] < other.pos[0]
        return self.pos[1] < other.pos[1]

map = []
units = []

for y, line in enumerate(lines):
    row = []
    for x, c in enumerate(line.strip("\n")):
        row.append(c == "#")
        if c in ["G", "E"]:
            unit = Unit()
            unit.isElf = c == "E"
            unit.pos = (x, y)
            units.append(unit)
    map.append(row)

neighbors = [(-1, -1), (0, -1), (1, -1), (-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]

def make_move_map(map, unit, units):
    move_map = []
    for r in map:
        move_map.append([-1] * len(r))

    next_candidates = [unit.pos]
    next_dist = 0
    done = False
    while not done:
        next_next = []
        done = True
        for nc in next_candidates:
            if 0 <= nc[1] and nc[1] < len(map) and 0 <= nc[0] and nc[0] < len(map[nc[1]]):
                if not map[nc[1]][nc[0]] and (move_map[nc[1]][nc[0]] == -1 or move_map[nc[1]][nc[0]] > next_dist):
                    has_unit = False
                    for ounit in units:
                        if nc == ounit.pos:
                            has_unit = True
                    if nc == unit.pos:
                        has_unit = False
                    if not has_unit:
                        done = False
                        move_map[nc[1]][nc[0]] = next_dist
                        for neighbor in neighbors:
                            next_next.append((nc[0] + neighbor[0], nc[1] + neighbor[1]))
        next_candidates = next_next
        next_dist += 1
    return move_map

def print_move_map(move_map):
    for row in move_map:
        row_str = ""
        for loc in row:
            if loc == -1:
                row_str += " "
            else:
                row_str += str(loc)
        print(row_str)

for _ in range(4):

    # sort
    units.sort()

    # move and fight
    for unit in units:
        move_map = make_move_map(map, unit, units)
        print_move_map(move_map)

print_map(map, units)
