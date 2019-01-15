#part 2
tests = [("51589", 9), 
         ("01245", 5), 
         ("92510", 18),
         ("59414", 2018),
         ("760221", 0)]

def print_board(board, positions):
    board_str = ""
    for i, d in enumerate(board):
        if i == positions[0]:
            board_str += "("+str(d)+") "
        elif i == positions[1]:
            board_str += "["+str(d)+"] "
        else:
            board_str += str(d) + " "
    print(board_str)

for test_nr, (t, res) in enumerate(tests):
    board = [3, 7]
    positions = [0, 1]

    test_list = []
    for c in t:
        test_list.append(int(c))

    done = False

    count = 2
    
    while not done:
        
        sum = 0

        for p in positions:
            sum += board[p]
        sumstr = str(sum)
        for c in sumstr:
            board.append(int(c))
            count += 1

            if board[-(len(test_list)+1):-1] == test_list:
                done = True
                pos_before = count - len(test_list) - 1
                print(t, pos_before, res, res == pos_before)
                print(board[-(len(test_list)+1):-1])
                print(test_list)

        for i, p in enumerate(positions):
            positions[i] = (p + board[p] + 1) % len(board)
