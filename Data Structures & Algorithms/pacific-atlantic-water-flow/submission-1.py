class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        m, n = len(heights[0]), len(heights)
        visited_pac = [[False] * m for _ in range(n)]
        visited_atl = [[False] * m for _ in range(n)]
        seen_pac = [[False] * m for _ in range(n)]
        seen_atl = [[False] * m for _ in range(n)]

        dirs = [(0,1), (1,0), (0,-1), (-1,0)]

        def dfs(visited, seen , r, c):
            for dr,dc in dirs:
                nr, nc = r+dr, c+dc
                if 0 <= nr< n and 0<= nc< m and heights[nr][nc] >= heights[r][c] and not seen[nr][nc]:
                    visited[nr][nc] = True
                    seen[nr][nc] = True
                    dfs(visited, seen, nr,nc)

            return 

        
        for r in range(n):
            visited_pac[r][0] = True
            seen_pac[r][0] = True
            dfs(visited_pac, seen_pac, r, 0)

            visited_atl[r][m-1] = True
            seen_atl[r][m-1] = True
            dfs(visited_atl, seen_atl, r, m-1)

        for c in range(m):
            visited_pac[0][c] = True
            seen_pac[0][c] = True
            dfs(visited_pac, seen_pac, 0,c)

            visited_atl[n-1][c] = True
            seen_atl[n-1][c] = True
            dfs(visited_atl, seen_atl, n-1, c)

        
        res = []

        for r in range(n):
            for c in range(m):
                if visited_pac[r][c] and visited_atl[r][c] :
                    res.append([r,c])

        return res


