class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        rows, cols = len(heights), len(heights[0])

        visited_pac = [[False] * cols for _ in range(rows)]
        visited_atl = [[False] * cols for _ in range(rows)]
        seen_pac = [[False] * cols for _ in range(rows)]
        seen_atl = [[False] * cols for _ in range(rows)]
        dirs = [(0,1), (1,0), (-1,0), (0,-1)]


        def dfs(visited, seen, r, c):

            for dr,dc in dirs:
                nr, nc = r+dr, c +dc
                if 0 <= nr< rows and 0<= nc < cols and heights[nr][nc] >= heights[r][c] and not seen[nr][nc] :
                    visited[nr][nc] = True
                    seen[nr][nc] = True
                    dfs(visited, seen,  nr, nc)
            return 
        
        for r in range(rows):
            visited_pac[r][0] = True
            seen_pac[r][0] = True
            dfs(visited_pac,seen_pac, r, 0)
            visited_atl[r][cols - 1] = True
            seen_atl[r][cols-1] = True
            dfs(visited_atl, seen_atl,  r, cols - 1)

        for c in range(cols):
            visited_pac[0][c] = True
            seen_pac[0][c] = True
            dfs(visited_pac, seen_pac,  0, c)
            visited_atl[rows-1][c] = True
            seen_atl[rows - 1][c] = True
            dfs(visited_atl, seen_atl,  rows-1, c)

        res = []

        for r in range(rows):
            for c in range(cols):
                if visited_pac[r][c] == True and visited_atl[r][c] == True:
                    res.append([r,c])


        return res

        