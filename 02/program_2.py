f = open("input.txt", "r")
lines = f.readlines()
f.close()

best_diff = 5000
best_l1 = ""
best_l2 = ""

for i1 in range(len(lines)):
    for i2 in range(i1 + 1, len(lines)):
        line_1 = lines[i1]
        line_2 = lines[i2]
        diff = 0
        for ci in range(len(line_1)):
            if line_1[ci] != line_2[ci]:
                diff += 1
        if diff < best_diff:
            best_diff = diff
            best_l1 = line_1
            best_l2 = line_2

print("best diff: ", best_diff)
print("best_l1: ", best_l1)
print("best_l2: ", best_l2)
