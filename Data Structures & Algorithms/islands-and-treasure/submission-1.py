class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]

        dirs = [(0,1), (1,0), (0,-1), (-1,0)]

        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r,c))
                    visited[r][c] = True

        while queue:
            n = len(queue)

            for i in range(n):
                r, c = queue.popleft()
                dist = grid[r][c]

                for dr, dc in dirs:
                    nr, nc = r +dr, c + dc

                    if 0 <= nr< rows and  0<= nc < cols and grid[nr][nc] != -1 and not visited[nr][nc]:
                        visited[nr][nc] = True
                        grid[nr][nc] = min(grid[nr][nc], dist +1 )
                        queue.append((nr, nc))

        
        print(grid)









