import math
import sys

def get_power(x, y, serial):
    rack_id = x + 10
    power_level = rack_id * y
    power_level += serial
    power_level *= rack_id
    power_level *= 0.01
    power_level = math.floor(power_level)
    power_level %= 10
    power_level -= 5
    return power_level

#print(get_power(3,5,8), 4)
#print(get_power(122,79,57), -5)
#print(get_power(217,196,39), 0)
#print(get_power(101,153,71), 4)

grid_serial_number = 5468

best_xs = 0
best_ys = 0
best_square_size = 0
best_score = 0

board = []
for i in range(300):
    board.append([0] * 300)

for x in range(1, 301):
    for y in range(1, 301):
        board[x-1][y-1] = get_power(x, y, grid_serial_number)

for square_size in range(1, 301):
    for ys in range(300 - square_size):

        score = 0

        for x in range(square_size):
            for y in range(ys, ys + square_size):
                score += board[x][y]

        for xs in range(0, 300 - square_size):

            if xs != 0:
                for y in range(ys, ys + square_size):
                    score -= board[xs-1][y]
                    score += board[xs + square_size - 1][y]

            if score > best_score:
                best_score = score
                best_xs = xs + 1
                best_ys = ys + 1
                best_square_size = square_size
    
    print(square_size)
    sys.stdout.flush()

print(best_xs, best_ys, best_square_size)
