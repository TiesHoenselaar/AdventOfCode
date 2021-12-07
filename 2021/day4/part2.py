with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

numbers = [int(x) for x in lines[0].split(',')]



# read boards

boards = []
board = []
for line in lines[1:]:
    if line == '':
        if len(board) > 0:
            boards.append(board)
            board = []
    else:

        board_row = [int(x) for x in line.split()]
        board.append(board_row)

boards.append(board)

# print(boards)

def check_board(board):
    for i in range(len(board)):
        if board[i][0] == board[i][1] == board[i][2] == board[i][3] == board[i][4] == -1:
            return True

        if board[0][i] == board[1][i] == board[2][i] == board[3][i] == board[4][i] == -1:
            return True

    return False


bingo = False
for number in numbers:

    if bingo:
        break

    
    for board in boards:
        for i in range(len(boards[0])):
            for j in range(len(boards[0][0])):
                if board[i][j] == number:
                    board[i][j] = -1

    new_boards = []
    for k, board in enumerate(boards):
        if check_board(board):
            # print(number, board)
            if len(boards) == 1:
                bingo = True
                bingo_board = boards[0]
                final_number = number
                break
        else:
            new_boards.append(board)

    boards = new_boards

total = 0

# print(bingo_board)
for i in range(len(bingo_board)):
    for j in range(len(bingo_board[0])):
        if bingo_board[i][j] != -1:
            total += bingo_board[i][j]

final_score = total * final_number

print('final_score:', final_score)
        

        
