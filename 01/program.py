import sys

frequency = 0
frequency_memory = []
f = open("input.txt", "r")
lines = f.readlines()
f.close()
for i in range(100000):
    if i % 10 == 0:
        print(".", end = "")
        sys.stdout.flush()
    for line in lines:
        for x in frequency_memory:
            if x == frequency:
                print(frequency)
                print("SAMMA!")
        frequency_memory.append(frequency)
        frequency += int(line)
print(frequency)
