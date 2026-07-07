class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        rows = 9 
        cols = 9 

        for r in range(rows):
            curr_row = [x for x in board[r] if x != '.']
            if len(curr_row) != len(set(curr_row)):

                return False

        for c in range(cols):
            curr_col = [x for r in range(rows) for x in board[r][c] if x != '.']
            if len(curr_col) != len(set(curr_col)):
                return False

        for r in range(0,9, 3):
            for c in range(0,9,3):
                grid = [board[i][j] for i in range(r,r+3) for j in range(c, c+3) if board[i][j] != '.']
                
                if len(grid) != len(set(grid)):
                    return False

        return True

                


        