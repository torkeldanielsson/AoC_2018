f = open("input.txt", "r")
lines = f.readlines()
f.close()

pairs = 0
triplets = 0

for line in lines:
    res = dict()
    for c in line:
        if c in res.keys():
            res[c] = res[c] + 1
        else:
            res[c] = 1
    pair = False
    triplet = False
    for key, value in res.items():
        if value == 2:
            pair = True
        if value == 3:
            triplet = True
    if pair:
        pairs += 1
    if triplet:
        triplets += 1

checksum = pairs * triplets

print("checksum: ", checksum)