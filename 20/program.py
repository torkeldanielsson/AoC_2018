f = open("test_4.txt", "r")
regex_ = f.read().strip().strip("^")
f.close()

regex = []
for c in regex_:
    regex.append(c)

def printmap(map):
    xmin = 999
    xmax = -999
    ymin = 999
    ymax = -999
    for loc in map.keys():
        x = int(loc.real)
        y = int(loc.imag)
        xmin = min(xmin, x)
        xmax = max(xmax, x)
        ymin = min(ymin, y)
        ymax = max(ymax, y)
    for y in range(ymin - 1, ymax + 2):
        rowstr = ""
        for x in range(xmin - 1, xmax + 2):
            loc = x + y*1j
            if loc in map:
                rowstr += map[loc]
            else:
                rowstr += "#"
        print(rowstr)

# ^ENWWW(NEEE|SSE(EE|N))$

map = {}

map[0] = 'X'

def parse(loc, regex):
    global map
    if len(regex) == 0:
        return
    c = regex.pop(0)
    if c == '$':
        print("end")
        return
    elif c == '(':
        parenthesis_depth = 1
        continuation = []
        while parenthesis_depth > 0:
            p = regex.pop(0)
            print("PARSING!", p)
            if p == '(':
                parenthesis_depth += 1
            elif p == ')':
                parenthesis_depth -= 1
            if p == '|' and parenthesis_depth == 1:
                # print("PARSE", continuation)
                parse(loc, continuation)
                continuation = []
            elif parenthesis_depth > 0:
                continuation.append(p)
        print("PARSE F", continuation)
        parse(loc, continuation)
    else:
        if c == 'N':
            loc -= 1j
            map[loc] = "-"
            loc -= 1j
        if c == 'S':
            loc += 1j
            map[loc] = "-"
            loc += 1j
        if c == 'W':
            loc -= 1
            map[loc] = "|"
            loc -= 1
        if c == 'E':
            loc += 1
            map[loc] = "|"
            loc += 1
        map[loc] = '.'
        print("")
        print(regex)
        print(loc)
        printmap(map)
    parse(loc, regex)

parse(0, regex)

print("")
printmap(map)
