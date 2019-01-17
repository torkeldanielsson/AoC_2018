import sys

f = open("test_2.txt", "r")
lines = f.readlines()
f.close()

class Unit:
    isElf = True
    hp = 200
    ap = 3
    pos = 0 + 0j

    def __lt__(self, other):
        if self.pos.imag == other.pos.imag:
            return self.pos.real < other.pos.real
        return self.pos.imag < other.pos.imag

height = len(lines)
width = len(lines[0].strip("\n"))

free_space = []
units = []
neighbors = [-1j, -1, 1, 1j]

for y, row in enumerate(lines):
    for x, c in enumerate(row.strip("\n")):
        loc = x + y*1j
        if c != "#":
            free_space.append(loc)
        if c in ["G", "E"]:
            unit = Unit()
            unit.isElf = c == "E"
            unit.pos = loc
            units.append(unit)

def print_map():
    for y in range(height):
        row_str = ""
        unit_str = " "
        for x in range(width):
            loc = x + y*1j
            isUnit = False
            for unit in units:
                if unit.pos == loc:
                    isUnit = True
                    unit_desc = "G"
                    if unit.isElf:
                        unit_desc = "E"
                    row_str += unit_desc
                    unit_str += unit_desc + str(unit.hp) + ", "

            if not isUnit:
                if loc not in free_space:
                    row_str += "#"
                else:
                    row_str += " "
        print(row_str + unit_str)

def make_move_map(pos, units):
    move_map = {}
    for y in range(height):
        for x in range(width):
            move_map[x + y*1j] = -1

    next_candidates = set()
    next_candidates.add(pos)
    next_dist = 0
    done = False
    while not done:
        next_next = set()
        done = True
        for nc in next_candidates:
            if nc in free_space and (move_map[nc] == -1 or move_map[nc] > next_dist):
                has_unit = False
                for unit in units:
                    if nc == unit.pos:
                        has_unit = True
                if nc == pos:
                    has_unit = False
                if not has_unit:
                    done = False
                    move_map[nc] = next_dist
                    for neighbor in neighbors:
                        next_next.add(nc + neighbor)
        next_candidates = next_next
        next_dist += 1
    return move_map

def print_move_map(move_map):
    for y in range(height):
        row_str = ""
        for x in range(width):
            loc = x + y*1j
            if not loc in free_space:
                row_str += "#"
            elif move_map[loc] == -1:
                row_str += " "
            else:
                row_str += str(move_map[loc])
            if not loc in free_space and move_map[loc] != -1:
                print("error")
        print(row_str)

bignum = 9999999999

print("Initially:")
print_map()

for round in range(24):

    # sort
    units.sort()

    # move and fight

    for unit in units:

        can_attack = False
        for n in neighbors:
            for i, enemy in enumerate(units):
                if enemy.isElf != unit.isElf:
                    if enemy.pos == unit.pos + n:
                        can_attack = True

        print(unit.pos, can_attack, unit.isElf)

        if not can_attack:
            move_map = make_move_map(unit.pos, units)

            best_target = 0
            best_target_score = bignum

            for enemy in units:
                if enemy.isElf != unit.isElf:
                    for n in neighbors:
                        neighbor = enemy.pos + n
                        if neighbor in move_map and move_map[neighbor] != -1 and move_map[neighbor] < best_target_score:
                            best_target = neighbor
                            best_target_score = move_map[neighbor]

            if best_target_score != bignum:

                target_move_map = make_move_map(best_target, units)

                best_next_move = 0
                best_next_move_score = bignum

                for n in neighbors:
                    neighbor = unit.pos + n
                    if (neighbor in target_move_map) and (target_move_map[neighbor] != -1) and (target_move_map[neighbor] < best_next_move_score):
                        best_next_move = neighbor
                        best_next_move_score = target_move_map[neighbor]
                
                if best_next_move != 0:
                    unit.pos = best_next_move

        # attack 

        attack = False
        best_target_i = 0
        best_hp = bignum
        for n in neighbors:
            for i, enemy in enumerate(units):
                if enemy.isElf != unit.isElf:
                    if enemy.pos == unit.pos + n:
                        if enemy.hp < best_hp:
                            attack = True
                            best_target_i = i
                            best_hp = enemy.hp
        if attack:
            units[best_target_i].hp -= unit.ap
            if units[best_target_i].hp <= 0:
                del units[best_target_i]

    print("\nAfter", round+1, "rounds:")
    print_map()
