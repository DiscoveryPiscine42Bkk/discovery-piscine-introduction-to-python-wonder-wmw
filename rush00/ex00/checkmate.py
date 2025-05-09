
class ChessBoard:
    def __init__(self, input_board):
        self.board = input_board.split()
        self.king_pos = []
        self.check = False
    
    def check_board(self, input_board):
         c_set = set("".join(input_board.split()))
         for c in c_set:
              if c not in ["P", "B", "R", "Q", "K", "."]:
                   return False
         if input_board.count("K") != 1:
              return False
         for row in self.board:
              if len(row) != len(self.board):
                   return False
         return True
         
    def get_king_pos(self):
        for r in range(len(self.board)):
            for c in range(len(self.board[0])):
                if self.board[r][c] == 'K':
                    self.king_pos = [r, c]
                    return

    def check_pawns(self, row, col):
        moves = [[-1, -1], [-1, 1]]
        for m in moves:
             if [row + m[0], col + m[1]] == self.king_pos:
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
    
    def check_all(self):
        self.get_king_pos()
        for r in range(len(self.board)):
            for c in range(len(self.board[0])):
                if self.board[r][c] == 'P':
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
    try:
        chess = ChessBoard(board)
        if chess.check_board(board):
            chess.check_all()
            chess.print_result()
        else:
            print("Error")
    except:
         print("Error")
