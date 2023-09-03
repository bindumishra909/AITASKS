import math

def evaluate(board):
    # Evaluates the current state of the game board
    # Returns +1 for AI win, -1 for human win, and 0 for a draw

    # Check rows for a win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            if board[i][0] == 'X':
                return -1
            elif board[i][0] == 'O':
                return 1

    # Check columns for a win
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == 'X':
                return -1
            elif board[0][i] == 'O':
                return 1

    # Check diagonals for a win
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == 'X':
            return -1
        elif board[0][0] == 'O':
            return 1

    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == 'X':
            return -1
        elif board[0][2] == 'O':
            return 1

    # No winner, check for a draw
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                return None

    return 0  # It's a draw


def minimax(board, depth, alpha, beta, isMaximizingPlayer):
    score = evaluate(board)

    # Check if the game has ended
    if score is not None:
        return score

    if isMaximizingPlayer:
        maxScore = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    maxScore = max(maxScore, minimax(board, depth + 1, alpha, beta, False))
                    board[i][j] = ' '

                    # Alpha-beta pruning
                    alpha = max(alpha, maxScore)
                    if beta <= alpha:
                        break
        return maxScore
    else:
        minScore = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    minScore = min(minScore, minimax(board, depth + 1, alpha, beta, True))
                    board[i][j] = ' '

                    # Alpha-beta pruning
                    beta = min(beta, minScore)
                    if beta <= alpha:
                        break
        return minScore


def getBestMove(board):
    bestScore = -math.inf
    bestMove = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                score = minimax(board, 0, -math.inf, math.inf, False)
                board[i][j] = ' '

                if score > bestScore:
                    bestScore = score
                    bestMove = (i, j)

    return bestMove


def printBoard(board):
    for i in range(3):
        print(' | '.join(board[i]))
        if i < 2:
            print('---------')
    print()


def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]

    while True:
        printBoard(board)

        # Human player's move
        while True:
            row = int(input("Enter the row (0-2): "))
            col = int(input("Enter the column (0-2): "))

            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == ' ':
                board[row][col] = 'X'
                break
            else:
                print("Invalid move. Try again.")

        # Check for game over
        result = evaluate(board)
        if result is not None:
            printBoard(board)
            if result == 1:
                print("AI wins!")
            elif result == -1:
                print("Human wins!")
            else:
                print("It's a draw!")
            break

        # AI player's move
        print("AI player is thinking...")
        row, col = getBestMove(board)
        board[row][col] = 'O'

        # Check for game… # Check for game over
        result = evaluate(board)
        if result is not None:
            printBoard(board)
            if result == -1:
                print("AI wins!")
            elif result == 1:
                print("player wins!")
            else:
                print("It's a draw!")
            break


if __name__ == "__main__":
    main()
