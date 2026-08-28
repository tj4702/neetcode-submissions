class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        m, n = len(grid), len(grid[0])

        islands = 0 
        visited = [[False] * (n) for _ in range(m)]
        dirs = [(0,1), (1,0), (-1,0,), (0,-1)]

        def dfs(r,c):

            visited[r][c] = True

            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if 0<= nr< m and 0<= nc<n and grid[nr][nc] == "1" and not visited[nr][nc]:
                    dfs(nr, nc)

            return 

        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1" and not visited[r][c]:
                    dfs(r, c)
                    islands +=1

        
        return islands





        