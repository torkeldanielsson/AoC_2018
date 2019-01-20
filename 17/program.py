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
    xmin = min(xmin, x - 1)
    xmax = max(xmax, x + 1)
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

while not done:
    did_flow = False
    for y in range(ymin - 9, ymax + 9):
        for x in range(xmin - 9, xmax + 9):
            loc = x + y*1j
            if map[loc] == '.':
                above = map[loc - 1j]
                below = map[loc + 1j]
                left = map[loc - 1]
                right = map[loc + 1]

                if above == '+' or above == '|':
                    did_flow = True
                    map[loc] = '|'
                if (below == '#' or below == '~') and (left == '|' or right == '|'):
                    did_flow = True
                    map[loc] = '|'
                if left == '|' and map[loc - 1 + 1j] == '#':
                    did_flow = True
                    map[loc] = '|'
                if right == '|' and map[loc + 1 + 1j] == '#':
                    did_flow = True
                    map[loc] = '|'

    did_fill = False

    if not did_flow:
        print("")
        printmap(map)
        sys.stdout.flush()
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
    
    if not did_flow and not did_fill:
        done = True


print("")
printmap(map)
