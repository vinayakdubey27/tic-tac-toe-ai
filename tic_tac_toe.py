HUMAN = "X"
AI = "O"

WIN_LINES = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6),
]

def new_board():
    return [" "] * 9


def print_board(board):

    cells = [c if c != " " else str(i + 1) for i, c in enumerate(board)]
    print()
    for r in range(3):
        a, b, c = cells[r * 3: r * 3 + 3]
        print(f" {a} | {b} | {c} ")
        if r < 2:
            print("---+---+---")
    print()


def legal_moves(board):
    return [i for i, c in enumerate(board) if c == " "]


def winner(board):
    for a, b, c in WIN_LINES:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]
    return None

def is_draw(board):
    return winner(board) is None and not legal_moves(board)

def minimax(board, is_ai_turn, depth):

    w = winner(board)
    if w == AI:
        return 10 - depth
    if w == HUMAN:
        return depth - 10
    if not legal_moves(board):
        return 0

    if is_ai_turn:
        best = -100
        for move in legal_moves(board):
            board[move] = AI
            best = max(best, minimax(board, False, depth + 1))
            board[move] = " "          # undo the move
        return best
    else:
        best = 100
        for move in legal_moves(board):
            board[move] = HUMAN
            best = min(best, minimax(board, True, depth + 1))
            board[move] = " "
        return best

def best_move(board):
    best_score, chosen = -100, None
    for move in legal_moves(board):
        board[move] = AI
        score = minimax(board, False, 1)
        board[move] = " "
        if score > best_score:
            best_score, chosen = score, move
    return chosen

def get_human_move(board):
    while True:
        raw = input("Your move (1-9): ").strip()
        if not raw.isdigit() or not 1 <= int(raw) <= 9:
            print("Please enter a number from 1 to 9.")
            continue
        move = int(raw) - 1
        if board[move] != " ":
            print("That cell is already taken. Try another.")
            continue
        return move

def ask_who_starts():
    while True:
        ans = input("Do you want to go first? (y/n): ").strip().lower()
        if ans in ("y", "yes"):
            return True
        if ans in ("n", "no"):
            return False
        print("Please type y or n.")

def play_game():
    board = new_board()
    human_turn = ask_who_starts()
    print(f"\nYou are {HUMAN}, the computer is {AI}.")

    while True:
        print_board(board)

        if human_turn:
            board[get_human_move(board)] = HUMAN
        else:
            print("Computer is thinking...")
            move = best_move(board)
            board[move] = AI
            print(f"Computer plays {move + 1}")

        w = winner(board)
        if w or is_draw(board):
            print_board(board)
            if w == HUMAN:
                print("Result: You WIN!")
            elif w == AI:
                print("Result: You LOSE. The computer wins.")
            else:
                print("Result: It's a DRAW.")
            return

        human_turn = not human_turn

def main():
    print("=== Tic-Tac-Toe vs Computer ===")
    try:
        while True:
            play_game()
            again = input("\nPlay again? (y/n): ").strip().lower()
            if again not in ("y", "yes"):
                print("Thanks for playing!")
                break
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")

if __name__ == "__main__":
    main()