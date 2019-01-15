import sys

f = open("input.txt", "r")
lines = f.readlines()
f.close()

#for line in lines:
#    print(line.strip())

class Cart:
    pos = (0, 0)
    direction = 0 # up down left right
    next_turn = 0 # left straight right
    prev_pos = (0, 0)
    has_collided = False

    def __lt__(self, other):
        if self.pos[1] == other.pos[1]:
            return self.pos[0] < other.pos[0]
        return self.pos[1] < other.pos[1]

board = []
carts = []

def direction_str(direction):
    if direction == 0:
        return "^"
    if direction == 1:
        return "v"
    if direction == 2:
        return "<"
    if direction == 3:
        return ">"

def print_board(board, carts, cx, cy):
    for y, l in enumerate(board):

        if cy >= 0 and (y-2>cy or y+2<cy):
            continue

        line = ""
        for x, c in enumerate(l):

            if cx >= 0 and (x-2>cx or x+2<cx):
                continue
        
            is_cart = False
            collision = False
            cart_symbol = "X"
            for cart in carts:
                if cart.pos == (x, y):
                    if is_cart:
                        collision = True
                    is_cart = True
                    cart_symbol = direction_str(cart.direction)
            if collision:
                line += "X"
            elif is_cart:
                line += cart_symbol
            else:
                line += c
        print(line)

for y, line in enumerate(lines):
    board_line = []
    for x, c in enumerate(line.strip("\n")):
        cart = False
        direction = 0
        if c == "<":
            cart = True
            direction = 2
            board_line.append("-")
        if c == ">":
            cart = True
            direction = 3
            board_line.append("-")
        if c == "^":
            cart = True
            direction = 0
            board_line.append("|")
        if c == "v":
            cart = True
            direction = 1
            board_line.append("|")
        
        if cart:
            #print("cart at ", x, y)
            new_cart = Cart()
            new_cart.pos = (x, y)
            new_cart.direction = direction
            carts.append(new_cart)
        else:
            board_line.append(c)
    board.append(board_line)

#print_board(board, carts, -1, -1)
#print("")

cart_to_follow = -1

while len(carts) > 1:

    collision_carts = []

    # sort carts
    #print("\n pre sort")

    #for c in carts:
    #    print("cart " + str(c.pos[0]) + " " + str(c.pos[1]))

    carts.sort()
    #print("\nsort")

    #for c in carts:
    #    print("cart " + str(c.pos[0]) + " " + str(c.pos[1]))
    #print("\n POST sort\n\n")

    # move
    for i, cart in enumerate(carts):

        if i == cart_to_follow:
            print("")
            print_board(board, carts, cart.pos[0], cart.pos[1])

        if cart.has_collided:
            continue

        cx = cart.pos[0]
        cy = cart.pos[1]

        if cart.direction == 0: # up
            cy -= 1
        if cart.direction == 1: # down
            cy += 1
        if cart.direction == 2: # left
            cx -= 1
        if cart.direction == 3: # right
            cx += 1
                
        cart.pos = (cx, cy)

        # collision
        for j, cart2 in enumerate(carts):
            if i != j and cart.pos == cart2.pos:
                print("COLLISION", cart.pos, i, j)
                collision_carts.append(i)
                collision_carts.append(j)
                cart.has_collided = True
                cart2.has_collided = True

        # turn
        p = board[cy][cx]

        if p == "/" and cart.direction == 0:
            cart.direction = 3
        elif p == "/" and cart.direction == 1:
            cart.direction = 2
        elif p == "/" and cart.direction == 2:
            cart.direction = 1
        elif p == "/" and cart.direction == 3:
            cart.direction = 0

        if p == "\\" and cart.direction == 0:
            cart.direction = 2
        elif p == "\\" and cart.direction == 1:
            cart.direction = 3
        elif p == "\\" and cart.direction == 2:
            cart.direction = 0
        elif p == "\\" and cart.direction == 3:
            cart.direction = 1
        
        if p == "+":
            if cart.direction == 0: # heading up
                if cart.next_turn == 0: # next left
                    cart.direction = 2
                if cart.next_turn == 2: # next right
                    cart.direction = 3
            elif cart.direction == 1: # heading down
                if cart.next_turn == 0: # next left
                    cart.direction = 3
                if cart.next_turn == 2: # next right
                    cart.direction = 2
            elif cart.direction == 2: # heading left
                if cart.next_turn == 0: # next left
                    cart.direction = 1
                if cart.next_turn == 2: # next right
                    cart.direction = 0
            elif cart.direction == 3: # heading right
                if cart.next_turn == 0: # next left
                    cart.direction = 0
                if cart.next_turn == 2: # next right
                    cart.direction = 1

            if cart.next_turn == 0: # next left
                cart.next_turn = 1
            elif cart.next_turn == 1: # next straight
                cart.next_turn = 2
            elif cart.next_turn == 2: # next right
                cart.next_turn = 0
    
    collision_carts = sorted(collision_carts, reverse=True)

    #print_board(board, carts)

    #print(collision_carts)

    for c in collision_carts:
        del carts[c]
    
    #print_board(board, carts)

print(carts[0].pos)