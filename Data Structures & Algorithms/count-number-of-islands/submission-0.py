class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        dirs = [(1,0), (0,1), (-1,0), (0,-1)]
        islands = 0 

        def dfs(r,c):
            for dr, dc in dirs:
                nr, nc = r+dr, c+dc 
                if 0 <= nr< rows and 0 <= nc < cols and not visited[nr][nc] and grid[nr][nc] == '1':
                    visited[nr][nc] = True
                    # change = True
                    dfs(nr, nc)

            return 


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and not visited[r][c]:
                    visited[r][c] = True
                    dfs(r,c)
                    islands += 1

        return islands
