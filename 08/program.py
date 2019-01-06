import sys
import copy
from datetime import datetime
import operator

f = open("input.txt", "r")
lines = f.readlines()
f.close()

input = lines[0].strip().split(" ")

print(input)

global all_meta_len
all_meta_len = 0

def parse_node(counter):
    children = int(input[counter])
    counter += 1
    meta_len = int(input[counter])
    counter += 1

    child_scores = []

    for i in range(children):
        (counter, child_score) = parse_node(counter)
        child_scores.append(child_score)

    metas = []

    for i in range(meta_len):
        this_meta = int(input[counter])

        metas.append(this_meta)

        global all_meta_len
        all_meta_len += this_meta

        counter += 1

    print(children, meta_len)

    for i, child_score in enumerate(child_scores):
        print("child", i, child_score)

    score = 0
    if children == 0:
        print("no children")
        for meta in metas:
            score += meta
    else:
        for meta in metas:
            meta_index = meta - 1
            if meta_index >= 0 and meta_index < len(child_scores):
                score += child_scores[meta_index]
                print("A", meta, meta_index, child_scores[meta_index])
            else:
                print("B")

    print("score", score)

    return (counter, score)

counter, score = parse_node(0)

print("part 1:", all_meta_len)

print("part 2:", score)