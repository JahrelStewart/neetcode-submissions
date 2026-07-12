class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dict_rows = {i: set() for i in range(9)}
        dict_cols = {i: set() for i in range(9)}
        dict_squares = {(x, y): set() for x in range(3) for y in range(3)}

        for row in range(9):
            for col in range(9):
                if board[row][col] == ".":
                    continue

                square = (row // 3, col // 3)
                if ((row in dict_rows and board[row][col] in dict_rows[row]) or
                   (col in dict_cols and board[row][col] in dict_cols[col]) or
                   (square in dict_squares and board[row][col] in dict_squares[square])):
                   return False

                dict_rows[row].add(board[row][col])
                dict_cols[col].add(board[row][col])
                dict_squares[square].add(board[row][col])
        
        return True