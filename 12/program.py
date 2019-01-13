
rules_ = ["...##",
         "..#..",
         ".#...",
         ".#.#.",
         ".#.##",
         ".##..",
         ".####",
         "#.#.#",
         "#.###",
         "##.#.",
         "##.##",
         "###..",
         "###.#",
         "####.", ]

rules = ["#..#.",
         "#.#..",
         "###..",
         ".#.##",
         "...#.",
         "##.#.",
         "###.#",
         "####.",
         ".##..",
         "#.##.",
         "#..##",
         "##...",
         "##.##",
         ".#..#",
         "..#.#",
         ".####",
         "..#..",
         ".##.#", ]


board = "..........#...#..##.......####.#..###..#.##..########.#.#...#.#...###.#..###.###.#.#..#...#.#..##..#######.##..................................................................................................................................................................................................................."
offset = -10

#print(" 0: " + board)

last_score = 0

for generation in range(100):
    next_board = ".."

    for i in range(len(board) - 2):
        rule_applies = False
        for rule in rules:
            if board[i:i+5] == rule:
                rule_applies = True

        if rule_applies:
            next_board += "#"
        else:
            next_board += "."
    
    board = next_board

    padding = ""
    if generation < 9:
        padding = " "
    #print(padding + str(generation + 1) + ": " + board)

    res = 0

    for i, c in enumerate(board):
        if c == "#":
            res += offset + i

    print(str(generation+1) + ": " + str(res) + ", diff: " + str(res - last_score))

    last_score = res
