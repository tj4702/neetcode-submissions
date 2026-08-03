class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]

        max_area = 0

        dirs = [(1,0), (0,1), (-1,0),(0,-1)]

        def area(r,c):
            if (r< 0 or r == rows or c < 0 or c == cols or grid[r][c] == 0 or visited[r][c] == True):
                return 0 
            
            visited[r][c] = True
            total = 1

            for dr,dc in dirs:
                nr, nc = r+ dr, c + dc
                total += area(nr, nc)
            
            return total

           

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and visited[r][c] == False:
                    curr_area = area(r,c)
                    max_area = max(max_area, curr_area)

        return max_area
                    
        