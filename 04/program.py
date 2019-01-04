import sys
import copy
from datetime import datetime
import operator

f = open("input.txt", "r")
lines = f.readlines()
f.close()

class Entry:
    timestamp = 0
    other_info = ""
    line = ""

entries = []

#datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')

#[1518-05-29 00:00] Guard #1151 begins shift
#[1518-10-29 00:18] falls asleep
#[1518-10-24 00:43] wakes up

for line in lines:
    parts1 = [p.replace("[", "").strip() for p in line.split("] ")]

    e = Entry()

    e.other_info = parts1[1]

    e.timestamp = datetime.strptime(parts1[0], "%Y-%m-%d %H:%M")
    e.line = line

    entries.append(copy.deepcopy(e))

entries.sort(key = operator.attrgetter('timestamp'))

guards = {}

current_guard_id = "-"

for e in entries:
    print(e.timestamp, e.other_info)

    if "Guard" in e.other_info:
        current_guard_id = e.other_info.split(" ")[1]

        print("found guard id: ", current_guard_id)

        if current_guard_id not in guards:
            print("first time seen!")
            guards[current_guard_id] = [0] * 60

    else:
        if "falls asleep" in e.other_info:
            sleep_minute = int(e.line.split(":")[1].split("]")[0])
        else:
            awake_minute = int(e.line.split(":")[1].split("]")[0])

            for minute in range(sleep_minute, awake_minute):
                guards[current_guard_id][minute] += 1

highest_sum = 0
most_sleepy_guard = 0
most_sleepy_guards_most_sleepy_minute = 0

for guard_id, minutes in guards.items():
    print(guard_id, minutes)

    sleep_sum = 0

    best_minute = 0
    most_sleepy_minute = 0

    minute_index = 0
    for m in minutes:
        sleep_sum += m
        if m > best_minute:
            best_minute = m
            most_sleepy_minute = minute_index
        minute_index += 1

    print(sleep_sum, best_minute, most_sleepy_minute)

    if sleep_sum > highest_sum:
        highest_sum = sleep_sum
        most_sleepy_guard = guard_id
        most_sleepy_guards_most_sleepy_minute = most_sleepy_minute

id = int(most_sleepy_guard.replace("#", ""))
print("part 1: ", most_sleepy_guard, most_sleepy_guards_most_sleepy_minute, id*most_sleepy_guards_most_sleepy_minute)
