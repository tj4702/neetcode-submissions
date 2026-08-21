class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        cols = set()
        rows = set()
        diag1 = set()
        diag2 = set()
        queen_cols = []

        res = []

        def backtrack(row):
            if row == n:
                board = []

                for i in range(n):
                    row = '.' * queen_cols[i] + 'Q' + '.' * (n-queen_cols[i] - 1)

                    board.append(row)

                res.append(board)

                return 

            
            for col in range(n):
                if col not in cols and (row- col) not in diag1 and (row+col) not in diag2:
                    queen_cols.append(col)
                    cols.add(col)
                    diag1.add(row-col)
                    diag2.add(row+col)
                    backtrack(row+1)
                    queen_cols.pop()
                    cols.remove(col)
                    diag1.remove(row-col)
                    diag2.remove(row+col)

        backtrack(0)

        return res


        
        