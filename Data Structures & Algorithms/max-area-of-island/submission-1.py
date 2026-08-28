class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        maxArea = 0 
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * (cols) for _ in range(rows)]
        dirs = [(0,1), (1,0), (-1,0), (0,-1)]

        def dfs(r, c):

            if r < 0 or r>= rows or c< 0 or c >= cols or visited[r][c] == True or grid[r][c] != 1:
                return 0 

            visited[r][c] = True
            tot = 1

            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                tot += dfs(nr, nc)
            
            return tot




        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and not visited[r][c]:
                    curr_area = dfs(r,c)
                    maxArea = max(maxArea, curr_area)

        return maxArea




        