
board = """\
        R...
        .K..
        ..P.
        ....\
        """


# split BOARD into LIST
rows = board.split('\n')
rows = [row.strip() for row in rows]
print(rows)

# check How many K-Kings in the board
if board.count("K") != 1:
    print("King more than 1")

# check characters are correct
row2 = set("".join(rows))
print(row2)

for i in row2:
    # print(i)
    if i not in ["P", "B", "R", "Q", "K", "."]:
        print("another character in the board")

# check square matrix or not
for row in rows:
    if len(row) != len(rows):
        print("not square matrix")
    # else:
    #     print(row, rows)
    #     print(len(rows))

#search for K-position
for row in range(len(rows)):
    for col in range(len(rows)):
        if rows[row][col] == 'K':
            K_pos = [row, col]
            # print(K_pos)

# check pawns move to catch King
P_moves = [ [1,-1], [-1,-1] ]
for p in P_moves:
    if [row+P_moves[0], col+P_moves[1]] == K_pos:
        print("K caught")

# check all Pieces current position
for r in range(len(rows)):
    for c in range(len(rows[o])):
        if rows[r][c] == "P":
            



