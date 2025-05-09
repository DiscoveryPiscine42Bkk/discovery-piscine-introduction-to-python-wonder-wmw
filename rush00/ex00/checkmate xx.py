class ChessBoard:
    def __init__(self, input_board):
        self.board = input_board.split()
        self.king_pos = []
        self.check = False

    def check_board_status(board):

        #split BOARD into LIST
        rows = board.split('\n')
        rows = [row.strip() for row in rows]
        print(rows)

        # check How many K-Kings in the board
        if board.count("K") != 1:
            print("King more than 1")
            return False

        # check characters are correct
        row2 = set("".join(rows))
        print(row2)

        for i in row2:
            # print(i)
            if i not in ["P", "B", "R", "Q", "K", "."]:
                print("another character in the board")
                return False

        # check square matrix or not
        for row in rows:
            if len(row) != len(rows):
                print("not square matrix")
                return False

    def get_K_position(self):
        #search for K-position
        for row in range(len(rows)):
            for col in range(len(rows)):
                if rows[row][col] == 'K':
                    K_pos = [row, col]
                    return False

    def check_Pawns(self, row, col):
        # check pawns move to catch King
        P_moves = [ [1,-1], [-1,-1] ]
        for p in P_moves:
            if [row+P_moves[0], col+P_moves[1]] == K_pos:
                print("K caught")
                return True
        return False

    def check_bishops(self, row, col):
        steps = [[-1, -1], [-1, 1], [1, -1], [1, 1]]
        moves = []
        for s in steps:
             for i in range(len(self.board)):
                  moves.append([s[0] * (i + 1), s[1] * (i + 1)])
                  
        for m in moves:
             if [row + m[0], col + m[1]] == self.king_pos:
                  return True
        return False
    
    def check_rooks(self, row, col):
        steps = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        moves = []
        for s in steps:
             for i in range(len(self.board)):
                  moves.append([s[0] * (i + 1), s[1] * (i + 1)])

        for m in moves:
             if [row + m[0], col + m[1]] == self.king_pos:
                  return True
        return False

    def check_queens(self, row, col):
        if self.check_rooks(row, col):
             return True
        elif self.check_bishops(row, col):
             return True
        else:
             return False
    
    def check_all_positions(self):
        # check all Pieces current position
        self.get_K_position()
        for r in range(len(self.rows)):
            for c in range(len(self.rows[o])):
                if self.rows[r][c] == "P":
                     if self.check_pawns(r, c):
                            self.check = True
                            return
                elif self.board[r][c] == 'R':
                    if self.check_rooks(r, c):
                            self.check = True
                            return
                elif self.board[r][c] == 'B':
                    if self.check_bishops(r, c):
                            self.check = True
                            return
                elif self.board[r][c] == 'Q':
                    if self.check_queens(r, c):
                            self.check = True
                            return
                    
    def print_result(self):
        if self.check:
            print("Success")
        else:
            print("Fail")

def checkmate(board):
    chess = ChessBoard(board)
    if chess.check_board_status(board):
        chess.check_all_positions()
        chess.print_result()
    else:
        print("Error")