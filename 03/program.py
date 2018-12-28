import sys
import copy

f = open("input.txt", "r")
lines = f.readlines()
f.close()

#1 @ 912,277: 27x20

class Region:
    i = 0
    x = 0
    y = 0
    w = 0
    h = 0

regions = []

for line in lines:
    parts1 = [p.replace("#", "").strip() for p in line.split("@")]
    r = Region()
    r.i = parts1[0]

    parts2 = parts1[1].split(": ")

    parts3 = parts2[0].split(",")
    r.x = int(parts3[0])
    r.y = int(parts3[1])

    parts4 = parts2[1].split("x")
    r.w = int(parts4[0])
    r.h = int(parts4[1])

    #print("p0: ", parts1[0], ", p1: ", parts1[1])
    #print(r.i, " ", r.x, " ", r.y, " ", r.w, " ", r.h)

    regions.append(r)

#for r in regions:
#    print("#", r.i, " @ ", r.x, ",", r.y, ": ", r.w, "x", r.h)

fabric = [[0 for x in range(1000)] for y in range(1000)] 

for r in regions:
    for x in range(r.x, r.x + r.w):
        for y in range(r.y, r.y + r.h):
            fabric[x][y] += 1

doubles = 0;

for x in range(1000):
    for y in range(1000):
        if fabric[x][y] > 1:
            doubles += 1

print("doubles: ", doubles)

for r in regions:
    ok = True
    for x in range(r.x, r.x + r.w):
        for y in range(r.y, r.y + r.h):
            if fabric[x][y] > 1:
                ok = False
    if ok:
        print("Ok claim:", r.i)
