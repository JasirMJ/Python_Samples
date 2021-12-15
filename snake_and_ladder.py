#program snake_and_ladder

def generate_snake_ladder_board(size):
    board = []
    for i in range(size):
        board.append([])
        for j in range(size):
            board[i].append(0)
    return board

print("Enter the size of the board")
size = int(input())

print("Enter the number of snakes")
snakes = int(input())

print("Enter the number of ladders")
ladders = int(input())

print(generate_snake_ladder_board(size))

#generate snakes in the board
for i in range(snakes):
    print("Enter the head and tail of the snake")
    start,end = map(int,input().split())
    board[start-1][end-1] = -1