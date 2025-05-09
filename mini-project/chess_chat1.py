board_input = [
    "R . . . Q . . .",
    ". . . . . . . .",
    ". . B . . . . .",
    ". . . . . . . .",
    ". . . . . . . .",
    ". . . . . . P .",
    ". . . . . . . .",
    ". . . . K . . ."
]

# Convert strings to 2D list
board_input = [row.split() for row in board_input]

# Count pieces in rows
row_counts = [sum(1 for cell in board_input ) for row in board_input]

# Count pieces in columns
col_counts = [sum(1 for row in board_input ) for col in board_input]

print(row_counts, col_counts)

# # Count total pieces and pieces by type
# from collections import Counter
# all_pieces = [cell for row in board for cell in row if cell != '.']
# piece_counts = Counter(all_pieces)
# total_pieces = len(all_pieces)

# # Display board with row counts
# print("Board with Row Counts:")
# for i, row in enumerate(board):
#     print(" ".join(row), f"| {row_counts[i]}")

# # Display column counts
# print("\nColumn Counts:")
# print(" ".join(str(c) for c in col_counts))

# # Display piece statistics
# print("\nTotal pieces:", total_pieces)
# print("Piece counts:")
# for piece, count in piece_counts.items():
#     print(f"  {piece}: {count}")
