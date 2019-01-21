import sys

f = open("input.txt", "r")
lines = f.read().splitlines()
f.close()

map = {}
width = len(lines[0])
height = len(lines)

for y, l in enumerate(lines):
    for x, c in enumerate(l):
        loc = x + y*1j
        if c != '\n':
            map[loc] = c

def printmap(map):
    for y in range(height):
        rowstr = ""
        for x in range(width):
            loc = x + y*1j
            rowstr += map[loc]
        print(rowstr)

def count_stuff(map):
    n_trees = 0
    n_lmbyrd = 0
    for y in range(height):
        for x in range(width):
            loc = x + y*1j
            if loc in map and map[loc] == '#':
                n_lmbyrd += 1
            if loc in map and map[loc] == '|':
                n_trees += 1
    return n_trees, n_lmbyrd

#printmap(map)

neighbors = [-1-1j, -1j, 1-1j, -1, 1, -1+1j, 1j, 1+1j]

map_history = []

print("(1000000000 - 407) % 28", ((1000000000 - 407) % 28) + 407)
print("(442 - 407) % 28", ((442 - 407) % 28) + 407)
number = 1000000000
number2 = number - 407
number3 = number2 % 27
number4 = number3 + 407
print(number, number2, number3, number4)

for i in range(500):
    new_map = {}
    for y in range(height):
        for x in range(width):
            loc = x + y*1j
            n_trees = 0
            n_lmbyrd = 0
            for n in neighbors:
                nloc = loc + n
                if nloc in map and map[nloc] == '#':
                    n_lmbyrd += 1
                if nloc in map and map[nloc] == '|':
                    n_trees += 1
            if map[loc] == '.' and n_trees >= 3:
                new_map[loc] = '|'
            elif map[loc] == '|' and n_lmbyrd >= 3:
                new_map[loc] = '#'
            elif map[loc] == '#' and (n_trees == 0 or n_lmbyrd == 0):
                new_map[loc] = '.'
            else:
                new_map[loc] = map[loc]
    
    map_history.append(map)

    for j, m in enumerate(map_history):
        if new_map == m:
            n_trees1, n_lmbyrd1 = count_stuff(new_map)
            n_trees2, n_lmbyrd2 = count_stuff(m)
            print("these maps are the same", i+1, j, n_trees1 * n_lmbyrd1, n_trees2 * n_lmbyrd2)
            # printmap(m)
            # printmap(new_map)

    map = new_map
    
    # print("")
    # printmap(map)

n_trees, n_lmbyrd = count_stuff(map)
print(n_trees * n_lmbyrd)