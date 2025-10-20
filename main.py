# Tic Tac Toe (very simple, 2 players)

BOARD = [" "] * 9
WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # cols
    (0, 4, 8), (2, 4, 6)              # diagonals
]

def show_board():
    b = BOARD
    print(f"\n {b[0]} | {b[1]} | {b[2]}")
    print("---|---|---")
    print(f" {b[3]} | {b[4]} | {b[5]}")
    print("---|---|---")
    print(f" {b[6]} | {b[7]} | {b[8]}\n")

def winner():
    for a, b, c in WIN_LINES:
        if BOARD[a] != " " and BOARD[a] == BOARD[b] == BOARD[c]:
            return BOARD[a]
    return None

def full():
    return all(cell != " " for cell in BOARD)

def get_move(player):
    while True:
        try:
            pos = int(input(f"Player {player}, choose 1-9: ")) - 1
            if pos not in range(9):
                print("Please enter a number from 1 to 9.")
            elif BOARD[pos] != " ":
                print("That spot is taken. Try again.")
            else:
                return pos
        except ValueError:
            print("Numbers only, please.")

def main():
    current = "X"
    print("Tic Tac Toe — Players: X and O")
    show_board()
    while True:
        move = get_move(current)
        BOARD[move] = current
        show_board()

        w = winner()
        if w:
            print(f"Player {w} wins!")
            break
        if full():
            print("It's a draw!")
            break

        current = "O" if current == "X" else "X"

if __name__ == "__main__":
    main()
