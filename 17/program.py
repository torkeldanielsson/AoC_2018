import sys

f = open("input.txt", "r")
lines = f.read().splitlines()
f.close()

xmin = 99999
xmax = -99999
ymin = 0
ymax = -99999

def set_maxmin(x, y):
    global xmin, xmax, ymin, ymax
    xmin = min(xmin, x - 20)
    xmax = max(xmax, x + 20)
    ymin = min(ymin, y)
    ymax = max(ymax, y)

def printmap(map):
    water_count = 0
    retained_count = 0
    for y in range(ymin, ymax + 1):
        rowstr = ""
        for x in range(xmin, xmax + 1):
            loc = x + y*1j
            if loc in map:
                rowstr += map[loc]
                if map[loc] == '|' or map[loc] == '~':
                    water_count += 1
                if map[loc] == '~':
                    retained_count += 1
            else:
                rowstr += "."
        print(rowstr)
    print("water count", water_count)
    print("retained count", retained_count)

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

# printmap(map)

done = False

neighbors = [-1, 1, 1j]

possible_flow_locs = set()
flow_locs = []

def flow_on_loc(loc):
    global xmin, xmax, ymin, ymax
    x = loc.real
    y = loc.imag
    if x > xmax + 8 or x < xmin -8 or y > ymax + 8 or y < ymin - 8:
        return False
    global map, possible_flow_locs
    
    #print("")
    #printmap(map)
    
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
            flow_locs.append(loc)
            for neighbor in neighbors:
                if not flow_on_loc(loc + neighbor):
                    possible_flow_locs.add(loc + neighbor)
    return did_flow

print_count = 0

flow_on_loc(500+ 1j)

while not done:

    did_flow = True
    
    while did_flow:
        did_flow = False
        bad_locs = []
        for loc in possible_flow_locs:
            if map[loc] != '.':
                bad_locs.append(loc)
        for b_loc in bad_locs:
            possible_flow_locs.remove(b_loc)
        possible_flow_locs_copy = possible_flow_locs.copy()
        for loc in possible_flow_locs_copy:
            if flow_on_loc(loc):
                did_flow = True

    did_fill = False

    bad_flow_locs = []
    for loc in flow_locs:
        if map[loc] != '|':
            bad_flow_locs.append(loc)
    for b_f_loc in bad_flow_locs:
        flow_locs.remove(b_f_loc)

    for loc in flow_locs:
        if map[loc] == '|' and map[loc - 1] == '#':
            possible_fill = True
            sweep_loc = loc
            while possible_fill:
                if map[sweep_loc] == '|' and map[sweep_loc + 1] == '#':
                    did_fill = True
                    itpos = sweep_loc
                    while map[itpos] == '|':
                        map[itpos] = '~'
                        itpos -= 1
                if map[sweep_loc] != '|':
                    possible_fill = False
                sweep_loc += 1
    
    if did_fill:
        print_count += 1
        if print_count%5000 == 0:
            print("")
            printmap(map)

    if not did_flow and not did_fill:
        done = True

print("")
printmap(map)
