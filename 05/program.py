import sys
import copy
from datetime import datetime
import operator

f = open("input.txt", "r")
lines = f.readlines()
f.close()

string = lines[0].strip()

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for c in alphabet:
    local_string = copy.deepcopy(string)
    local_string = local_string.replace(c, "").replace(c.lower(), "")

    didReplace = True

    while didReplace:
        didReplace = False
        for i in range(0, len(local_string) - 1):
            if ((local_string[i].isupper() and local_string[i + 1].islower()) or (local_string[i].islower() and local_string[i + 1].isupper())) and (local_string[i].upper() == local_string[i + 1].upper()):
                match = local_string[i] + local_string[i + 1]
                #print(i, match)
                didReplace = True
                local_string = local_string.replace(match, "")
                break

    print(c, "len: ", len(local_string))
    sys.stdout.flush()

