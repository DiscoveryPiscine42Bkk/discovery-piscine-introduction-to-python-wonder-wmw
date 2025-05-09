# def parse_board(board_lines):
#     board = [list(line.strip()) for line in board_lines if line.strip()]
#     size = len(board)

#     # Check square board validity
#     if not all(len(row) == size for row in board):
#         raise ValueError("Board is not square.")
    
#     # Locate king
#     king_positions = [(i, row.index('K')) for i, row in enumerate(board) if 'K' in row]
#     if len(king_positions) != 1:
#         raise ValueError("There must be exactly one king.")
#     king_pos = king_positions[0]

#     return board, size, king_pos

# def is_in_bounds(x, y, size):
#     return 0 <= x < size and 0 <= y < size

# def can_attack_king(board, size, king_pos, x, y, piece):
#     directions = []

#     if piece == 'R':
#         directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
#     elif piece == 'B':
#         directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
#     elif piece == 'Q':
#         directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
#                       (-1, -1), (-1, 1), (1, -1), (1, 1)]
#     elif piece == 'P':
#         # Assume pawn captures diagonally upward
#         directions = [(-1, -1), (-1, 1)]
#     else:
#         return False  # Not a recognized attacking piece

#     for dx, dy in directions:
#         nx, ny = x + dx, y + dy
#         while is_in_bounds(nx, ny, size):
#             cell = board[nx][ny]
#             if (nx, ny) == king_pos:
#                 return True
#             if cell != '.':
#                 break  # First piece blocks the path
#             if piece == 'P':  # Pawn captures only one square
#                 break
#             nx += dx
#             ny += dy
#     return False

# def check_king_in_check(board_lines):
#     try:
#         board, size, king_pos = parse_board(board_lines)
#     except ValueError as e:
#         print("Error:", e)
#         return

#     for x in range(size):
#         for y in range(size):
#             piece = board[x][y]
#             if piece in ['R', 'B', 'Q', 'P']:
#                 if can_attack_king(board, size, king_pos, x, y, piece):
#                     print("Success")
#                     return
#     print("Fail")

# Example usage
# board_input = [
#     "R . . . Q . . .",
#     ". . . . . . . .",
#     ". . B . . . . . .",
#     ". . . . . . . .",
#     ". . . . . . . .",
#     ". . . . . . P .",
#     ". . . . . . . .",
#     ". . . . K . . ."
# ]

# check_king_in_check(board_input)

#     board = [list(line.strip()) for line in board_lines if line.strip()]
#     size = len(board)

#     # Check square board validity
#     if not all(len(row) == size for row in board):
#         raise ValueError("Board is not square.")
    
#     # Locate king
#     king_positions = [(i, row.index('K')) for i, row in enumerate(board) if 'K' in row]
#     if len(king_positions) != 1:
#         raise ValueError("There must be exactly one king.")
#     king_pos = king_positions[0]

# size = len(board_input)
# print(size)
# king_pos = None

# for i in range(size):
#     for j in range(size):
#         if board_input[i][j] != 'K':
#             king_pos = (i, j)
#             print(board_input[i][j]) 
#             break
        
#     if king_pos:
#         break

# if not king_pos:
#     print("Error: No King found.")

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [11, 22, 33, 44]]

# rows = len(matrix)
# cols = len(matrix[0])

# print("Rows:", rows)
# print("Columns:", cols)

# for i in range(matrix[0:]):
#     print(matrix[i])

# if rows == cols:
#     print("It's a square matrix.")
# else:
#     print("Not a square matrix.")


# matrix = [
#     ['a', 'b', 'c'],
#     ['d', 'e', 'f'],
#     ['g', 'h', 'i', 'j']
# ]

# # Number of rows and columns
# rows = len(matrix)
# cols = len(matrix[0])

# print("Number of rows:", rows)
# print("Number of columns:", cols)

# # Count characters in each row
# print("\nCharacters in each row:")
# for i, row in enumerate(matrix):
#     count = sum(len(str(elem)) for elem in row)
#     print(f"Row {i + 1}: {count} characters")

#     print(i, row)
#     print("enumerate ",enumerate(matrix))


# # Count characters in each column
# print("\nCharacters in each column:")
# for col in range(cols):
#     count = sum(len(str(matrix[row][col])) for row in range(rows))
#     print(f"Column {col + 1}: {count} characters")


board = [
    "R . . . Q . . .",
    ". . . . . . . .",
    ". . B . . . . . .",
    ". . . . . . . .",
    ". . . . . . . .",
    ". . . . . . P .",
    ". . . . . . . .",
    ". . . . K . . ."
    ]

# for i, row in enumerate(board):
#     count = sum(len(str(elem)) for elem in row)
#     print(f"Row {i + 1}: {count} characters")

# for n in range(len(board))
board = [row.split() for row in board]
print(board, end="")