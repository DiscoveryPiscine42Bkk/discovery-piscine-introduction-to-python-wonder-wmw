def is_king_in_check(board):
    try:
        size = len(board)
        # Locate the king
        king_pos = None
        for i in range(size):
            for j in range(size):
                if board[i][j] == 'K':
                    king_pos = (i, j)
                    print(king_pos)   #####
                    break
            if king_pos:
                break
        if not king_pos:
            print("Error: No King found.")
            return

        directions = {
            'R': [(-1, 0), (1, 0), (0, -1), (0, 1)],
            'B': [(-1, -1), (-1, 1), (1, -1), (1, 1)],
            'Q': [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)],
            'P': [(-1, -1), (-1, 1)],  # assuming pawns move upward (toward the king)
        }

        for i in range(size):
            for j in range(size):
                piece = board[i][j]
                if piece not in directions:
                    continue
                for dx, dy in directions[piece]:
                    x, y = i + dx, j + dy
                    while 0 <= x < size and 0 <= y < size:
                        if board[x][y] == 'K':
                            print("Success")
                            return
                        if board[x][y] != '.':
                            break  # only first piece in path is capturable
                        if piece == 'P':
                            break  # pawns don't slide
                        x += dx
                        y += dy
        print("Fail")
    except Exception:
        # If anything unexpected happens
        return


board = [
    ['.', '.', '.', '.', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', 'Q', '.', '.', '.'],
    ['.', '.', '.', '.', '.'],
    ['.', '.', '.', 'K', '.']
]
is_king_in_check(board)  # Should print "Success"


