def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]
    
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]
    
   
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    
    return None

def main():
    board = [[' ']*3 for _ in range(3)]
    players = ['X', 'O']
    current_player = 0

    print("Welcome to Tic Tac Toe!")
    print_board(board)

    while True:
        row = int(input("Player {} row (1-3): ".format(players[current_player])))
        col = int(input("Player {} column (1-3): ".format(players[current_player])))

        if row < 1 or row > 3 or col < 1 or col > 3:
            print("Invalid input. Row and column must be between 1 and 3.")
            continue
        
        if board[row-1][col-1] != ' ':
            print("That cell is already taken. Try again.")
            continue
        
        board[row-1][col-1] = players[current_player]
        print_board(board)

        winner = check_winner(board)
        if winner:
            print("Player {} wins!".format(winner))
            break
        
        if all(cell != ' ' for row in board for cell in row):
            print("It's a draw!")
            break
        
        current_player = (current_player + 1) % 2

if __name__ == "__main__":
    main()
