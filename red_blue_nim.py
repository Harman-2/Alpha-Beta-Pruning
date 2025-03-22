import sys

# Defining constants for player and version
COMPUTER = "computer"
HUMAN = "human"
STANDARD = "standard"
MISERE = "misere"

def display(red, blue):
    """Displays the current state of the game."""
    print(f"Red: {red} Blue: {blue}")

def user_move(red, blue, version):
    """Gets the move from the human user."""
    while True:
        pile = input("Choose a pile (red or blue): ")
        if pile not in ["red", "blue"]:
            print("Incorrect pile. Choose 'red' or 'blue'.")
            continue
        cnt = int(input(f"Enter the number of {pile} marbles to remove: "))
        if pile == "red" and cnt > red:
            print("Incorrect move. Not enough red marbles.")
            continue
        if pile == "blue" and cnt > blue:
            print("Incorrect move. Not enough blue marbles.")
            continue
        return pile, cnt

def evaluate(red, blue, version):
    """Evaluates the score based on red and blue marbles."""
    if version == STANDARD:
        return -2 * red - 3 * blue
    elif version == MISERE:
        return 2 * red + 3 * blue

def min_max_alpha_beta(red, blue, version, depth, maximizing_player, alpha, beta):
    """ Defines MinMax search with alpha beta pruning  """
    if red == 0 and blue == 0:
        return evaluate(red, blue, version)

    if maximizing_player:
        max_eval = float('-inf')
        if red > 0:
            max_eval = max(max_eval, min_max_alpha_beta(red - 1, blue, version, depth - 1, False, alpha, beta))
        if blue > 0:
            max_eval = max(max_eval, min_max_alpha_beta(red, blue - 1, version, depth - 1, False, alpha, beta))
        alpha = max(alpha, max_eval)
        return max_eval

    else:
        min_eval = float('inf')
        if red > 0:
            min_eval = min(min_eval, min_max_alpha_beta(red - 1, blue, version, depth - 1, True, alpha, beta))
        if blue > 0:
            min_eval = min(min_eval, min_max_alpha_beta(red, blue - 1, version, depth - 1, True, alpha, beta))
        beta = min(beta, min_eval)
        return min_eval

def computer_move(red, blue, version, depth):
    """ Defines the computer move order. """
    alpha = float('-inf')
    beta = float('inf')
    best_value = float('-inf')
    best_move = None

    if version == STANDARD:
        move_order = [("blue", blue), ("red", red)]
    elif version == MISERE:
        move_order = [("red", red), ("blue", blue)]

    for pile, cnt in move_order:
        if pile == "red" and cnt > 0:
            value = min_max_alpha_beta(red - 1, blue, version, depth, False, alpha, beta)
        elif pile == "blue" and cnt > 0:
            value = min_max_alpha_beta(red, blue - 1, version, depth, False, alpha, beta)

        if value > best_value:
            best_value = value
            best_move = (pile, cnt)

    return best_move

def ply_red_blue_nim(red, blue, version, first_player, depth):
    """ Displays all moves and shows the winner. """
    while red > 0 and blue > 0:
        display(red, blue)
        if first_player == COMPUTER:
            print("Computer's turn:")
            move = computer_move(red, blue, version, depth)
            pile, cnt = move
            print(f"Computer removes {cnt} {pile} marble(s).")
            if pile == "red":
                red -= cnt
            else:
                blue -= cnt
        else:
            print("Human's turn:")
            pile, cnt = user_move(red, blue, version)
            if pile == "red":
                red -= cnt
            else:
                blue -= cnt

        first_player = COMPUTER if first_player == HUMAN else HUMAN

    display(red, blue)
    winner = COMPUTER if first_player == HUMAN else HUMAN
    score = evaluate(red, blue, version)

    if score < 0:
        print(f"{winner} loses with a score of {-score}.")
    else:
        print(f"{winner} wins with a score of {score}.")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("red_blue_nim.py <num-red> <num-blue> [version] [first-player] [depth]")
    else:
        num_red = int(sys.argv[1])
        num_blue = int(sys.argv[2])
        version = sys.argv[3] if len(sys.argv) > 3 else STANDARD
        first_player = sys.argv[4] if len(sys.argv) > 4 else COMPUTER
        depth = int(sys.argv[5]) if len(sys.argv) > 5 else 0
        ply_red_blue_nim(num_red, num_blue, version, first_player, depth)
