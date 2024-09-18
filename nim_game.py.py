import sys

def game_over(state, is_misere):
    red, blue = state
    if is_misere:
        return red == 0 or blue == 0 
    return red == 0 and blue == 0


def evaluate(state):
    red, blue = state
    return 2 * red + 3 * blue  

def get_legal_moves(state):
    red, blue = state
    moves = []
    if red >= 2:
        moves.append((-2, 0))  
    if blue >= 2:
        moves.append((0, -2))  
    if red >= 1:
        moves.append((-1, 0))  
    if blue >= 1:
        moves.append((0, -1))  
    return moves

def apply_move(state, move):
    red, blue = state
    return red + move[0], blue + move[1]  


def human_move(state):
    while True:
        print(f"Current state: {state[0]} red marbles, {state[1]} blue marbles")
        move = input("Enter your move (e.g., '-1 0' to remove 1 red, '0 -2' to remove 2 blue): ")
        try:
            move = tuple(map(int, move.split()))
            if move in get_legal_moves(state):
                return apply_move(state, move)
            else:
                print("Invalid move. Try again.")
        except:
            print("Invalid input. Please enter two integers separated by a space.")

def minmax_ab(state, depth, alpha, beta, maximizing_player, is_misere):
    if game_over(state, is_misere) or depth == 0:
        return evaluate(state)

    if maximizing_player:
        max_eval = -float('inf')
        for move in get_legal_moves(state):
            eval = minmax_ab(apply_move(state, move), depth-1, alpha, beta, False, is_misere)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:  
                break
        return max_eval
    else:
        min_eval = float('inf')
        for move in get_legal_moves(state):
            eval = minmax_ab(apply_move(state, move), depth-1, alpha, beta, True, is_misere)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha: 
                break
        return min_eval

def computer_move(state, depth, is_misere):
    best_move = None
    best_value = -float('inf')
    for move in get_legal_moves(state):
        new_state = apply_move(state, move)
        move_value = minmax_ab(new_state, depth-1, -float('inf'), float('inf'), False, is_misere)
        if move_value > best_value:
            best_value = move_value
            best_move = move
    print(f"Computer removes {abs(best_move[0])} red marbles and {abs(best_move[1])} blue marbles.")
    return apply_move(state, best_move)

def nim_game(num_red, num_blue, version='standard', first_player='computer', depth=4):
    is_misere = (version == 'misere')
    state = (num_red, num_blue)
    
    if first_player == 'human':
        turn = 'human'
    else:
        turn = 'computer'

    while not game_over(state, is_misere):
        if turn == 'human':
            state = human_move(state)
            turn = 'computer'
        else:
            state = computer_move(state, depth, is_misere)
            turn = 'human'

    print(f"Game Over! Final state: {state[0]} red marbles, {state[1]} blue marbles")
    if is_misere:
        print("Human wins!" if turn == 'computer' else "Computer wins!")
    else:
        score = evaluate(state)
        print(f"Final score: {score} points")

if __name__ == "__main__":
    if len(sys.argv) > 1:  
        num_red = int(sys.argv[1])
        num_blue = int(sys.argv[2])
        version = sys.argv[3] if len(sys.argv) > 3 else 'standard'
        first_player = sys.argv[4] if len(sys.argv) > 4 else 'computer'
        depth = int(sys.argv[5]) if len(sys.argv) > 5 else 4
    else: 
        num_red = int(input("Enter the number of red marbles: "))
        num_blue = int(input("Enter the number of blue marbles: "))
        version = input("Enter the version (standard or misere): ") or 'standard'
        first_player = input("Who goes first (human or computer): ") or 'computer'
        depth = int(input("Enter the search depth for AI: ") or 4)

    nim_game(num_red, num_blue, version, first_player, depth)
