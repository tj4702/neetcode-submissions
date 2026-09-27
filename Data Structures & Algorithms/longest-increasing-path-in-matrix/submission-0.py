class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        m,n = len(matrix), len(matrix[0])

        memo = {}

        dirs = [(0,1), (1,0), (-1,0), (0,-1)]

        def dfs(r, c):
            if (r,c) in memo:
                return memo[(r,c)]

            best = 1 

            for dr, dc in dirs:
                nr, nc = dr+r, dc +c

                if 0<= nr < m and 0<=nc < n and matrix[nr][nc] > matrix[r][c]:
                    best = max(best , 1 + dfs(nr, nc))

            memo[(r,c)] = best

            return best 

        res = 0


        for r in range(m):
            for c in range(n):
                res = max(res, dfs(r, c))

        return res





        