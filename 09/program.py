import sys
from collections import deque

playerss =             [  9,   10,     13,   17,    21,    30,    412,        412 ]
game_lengths =         [ 25, 1618,   7999, 1104,  6111,  5807,  71646,    7164600 ]
correct_answers =      [ 32, 8317, 146373, 2764, 54718, 37305, 439635, 3562722971 ]

#playerss =             [  9 ]
#game_lengths =         [ 25 ]
#correct_answers =      [ 32 ]

for game_number in range(len(game_lengths)):

    players = playerss[game_number]
    game_length = game_lengths[game_number]

    board = deque([])

    player_scores = [0] * players

    current_player = 0

    for turn in range(0, game_length + 1):

        current_player = turn % players

        if turn != 0 and turn%23 == 0:
            player_scores[current_player] += turn
            board.rotate(-7)
            player_scores[current_player] += board.pop()
        else:
            board.rotate(2)
            board.append(turn)

        #print_string = "[" + str(current_player) + "] "
        #for m in board:
        #    print_string += str(m) + " "
        #print(print_string)

    high_score = 0
    for p in player_scores:
        if p > high_score:
            high_score = p

    res = "Ok"
    if correct_answers[game_number] != high_score:
        res = "ERROR"

    print("game", game_number, "players", players, "game_length", game_length, "high_score", high_score, "result", res)
    sys.stdout.flush()
