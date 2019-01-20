import sys

f = open("test.txt", "r")
lines = f.read().splitlines()
f.close()

xmin = 99999
xmax = -99999
ymin = 0
ymax = -99999

def set_maxmin(x, y):
    global xmin, xmax, ymin, ymax
    xmin = min(xmin, x)
    xmax = max(xmax, x)
    ymin = min(ymin, y)
    ymax = max(ymax, y)

def printmap(map):
    water_count = 0
    for y in range(ymin, ymax + 1):
        rowstr = ""
        for x in range(xmin, xmax + 1):
            loc = x + y*1j
            if loc in map:
                rowstr += map[loc]
                if map[loc] == '|' or map[loc] == '~':
                    water_count += 1
            else:
                rowstr += "."
        print(rowstr)
    print("water count", water_count)

map = {}
map[500] = '+'

# x=495, y=2..7
# y=7, x=495..501

done = False

for line in lines:
    if not done and line[0] == "x":
        parts = line.strip("x=").split(", y=")
        x = int(parts[0])
        yparts = parts[1].split("..")
        for y in range(int(yparts[0]), int(yparts[1]) + 1):
            map[x + y*1j] = '#'
            set_maxmin(x, y)
    if not done and line[0] == "y":
        parts = line.strip("y=").split(", x=")
        y = int(parts[0])
        xparts = parts[1].split("..")
        for x in range(int(xparts[0]), int(xparts[1]) + 1):
            map[x + y*1j] = '#'
            set_maxmin(x, y)

for y in range(ymin - 10, ymax + 10):
    for x in range(xmin - 10, xmax + 10):
        loc = x + y*1j
        if loc not in map:
            map[loc] = '.'

printmap(map)

done = False

neighbors = [-1j, -1, 1, 1j]

def flow_on_loc(loc, map, possible_next_locs):
    did_flow = False
    if map[loc] == '.':
        above = map[loc - 1j]
        below = map[loc + 1j]
        left = map[loc - 1]
        right = map[loc + 1]

        flow = False
        if above == '+' or above == '|':
            flow = True
        if below == '~' and (left == '|' or right == '|'):
            flow = True
        if left == '|' and (map[loc - 1 + 1j] == '#' or map[loc - 1 + 1j] == '~'):
            flow = True
        if right == '|' and (map[loc + 1 + 1j] == '#' or map[loc + 1 + 1j] == '~'):
            flow = True
        
        if flow:
            did_flow = True
            map[loc] = '|'
            for neighbor in neighbors:
                possible_next_locs.append(loc + neighbor)
    return did_flow

print_count = 0

while not done:
    did_flow = False

    possible_next_locs = []

    for y in range(ymin - 9, ymax + 9):
        for x in range(xmin - 9, xmax + 9):
            loc = x + y*1j
            if flow_on_loc(loc, map, possible_next_locs):
                did_flow = True

    inner_did_flow = True
    while inner_did_flow:
        inner_did_flow = False
        next_possible_next_locs = []
        for low in possible_next_locs:
            if flow_on_loc(loc, map, possible_next_locs):
                inner_did_flow = True
        possible_next_locs = next_possible_next_locs

    did_fill = False

    if not did_flow:
        for y in range(ymin, ymax):
            possible_begin_fill = False
            for x in range(xmin, xmax):
                loc = x + y*1j
                here = map[loc]
                above = map[loc - 1j]
                below = map[loc + 1j]
                left = map[loc - 1]
                right = map[loc + 1]

                if here == '|' and left == '#':
                    possible_begin_fill = True
                if possible_begin_fill and here == '|' and right == '#':
                    did_fill = True
                    itpos = loc
                    while map[itpos] == '|':
                        map[itpos] = '~'
                        itpos -= 1
                if here != '|':
                    possible_begin_fill = False
    
    if did_fill:
        print_count += 1
        if print_count%20 == 0:
            print("")
            printmap(map)
            sys.stdout.flush()

    if not did_flow and not did_fill:
        done = True

print("")
printmap(map)
