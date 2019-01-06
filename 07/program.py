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

#for d in deps:
#    print(d.step, d.enables)
#print("")

graph = {}

for n in nodes:
    prereqs = []
    for d in deps:
        if d.enables == n:
            prereqs.append(d.step)
    graph[n] = prereqs

#for n, p in graph.items():
#    print(n, p)
#print("")

procedure = ""
completed_steps = []

allDone = False

second = 0

class Worker:
    isWorking = False
    task = " "
    secondsLeft = 0

workers = []
for i in range(5):
    workers.append(Worker())

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

baseTaskCost = 60

while not allDone:
    allDone = True

    for worker in workers:
        if worker.isWorking:
            worker.secondsLeft -= 1
            if worker.secondsLeft <= 0:
                worker.isWorking = False
                completed_steps.append(worker.task)
                worker.task = " "
                procedure += worker.task

    possibleNextSteps = []

    for n, p in graph.items():
        #print(n, p)
        if n in completed_steps:
            continue
        allDone = False
        isBeingWorkedOn = False
        for worker in workers:
            if worker.task == n:
                isBeingWorkedOn = True
        if isBeingWorkedOn:
            continue
        if set(p).issubset(set(completed_steps)):
            possibleNextSteps.append(n)

    possibleNextSteps.sort()

    for worker in workers:
        if len(possibleNextSteps) > 0:
            if not worker.isWorking:
                worker.isWorking = True
                worker.task = possibleNextSteps[0]
                del possibleNextSteps[0]
                worker.secondsLeft = baseTaskCost + 1 + alphabet.find(worker.task)
                #print(worker.task, alphabet, "location:", alphabet.find(worker.task), worker.secondsLeft)

    taskString = ""
    for worker in workers:
        taskString += worker.task + " "

    print("second", second, taskString, completed_steps)

    if not allDone:
        second += 1

print("procedure", procedure)

print("seconds:", second)
