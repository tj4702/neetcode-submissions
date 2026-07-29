class Solution:
    def solve(self, board: List[List[str]]) -> None:


        rows, cols = len(board), len(board[0])

        def dfs(nr, nc):

            if nr < 0 or nr >= rows or 0 > nc or nc >= cols or board[nr][nc] != 'O':
                return 
            board[nr][nc] = 'T'
            dfs(nr-1, nc)
            dfs(nr+1, nc)
            dfs(nr, nc-1)
            dfs(nr, nc+1)


        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O' and ( (r == 0 or r == rows - 1) or (c == 0 or c == cols -1)):
                    dfs(r,c)

        
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                if board[r][c] == 'T':
                    board[r][c] = 'O'

