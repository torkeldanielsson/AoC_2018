#part 1
tests = [(9, "5158916779"), (5, "0124515891"), (18, "9251071085"), (2018, "5941429882"), (760221, "1411383621")]

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
    #print("\nTurns: ", t)
    
    #print_board(board, positions)
    
    while len(board) < (t + 10):
        
        sum = 0

        for p in positions:
            sum += board[p]
        sumstr = str(sum)
        for c in sumstr:
            board.append(int(c))

        for i, p in enumerate(positions):
            positions[i] = (p + board[p] + 1) % len(board)

        #print_board(board, positions)

    myres = ""
    reslist = board[t:t+10]
    for r in reslist:
        myres += str(r)
    print(t, len(board), res, myres, res == myres)
