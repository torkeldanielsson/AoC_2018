import sys
import copy
from datetime import datetime
import operator

f = open("input.txt", "r")
lines = f.readlines()
f.close()

class Dependency:
    step = ""
    enables = ""

#Step C must be finished before step A can begin.

deps = []
nodes = set()

for line in lines:
    parts = line.strip().split(" ")
    d = Dependency()
    d.step = parts[1]
    d.enables = parts[7]
    deps.append(d)
    nodes.add(d.step)
    nodes.add(d.enables)

for d in deps:
    print(d.step, d.enables)
print("")

graph = {}

for n in nodes:
    prereqs = []
    for d in deps:
        if d.enables == n:
            prereqs.append(d.step)
    graph[n] = prereqs

for n, p in graph.items():
    print(n, p)
print("")

procedure = ""
completed_steps = []

allDone = False

while not allDone:
    allDone = True

    possibleNextSteps = []

    for n, p in graph.items():
        print(n, p)
        if n in completed_steps:
            continue
        if set(p).issubset(set(completed_steps)):
            allDone = False
            possibleNextSteps.append(n)

    possibleNextSteps.sort()

    if len(possibleNextSteps) > 0:
        procedure += possibleNextSteps[0]
        completed_steps.append(possibleNextSteps[0])

print(procedure)
