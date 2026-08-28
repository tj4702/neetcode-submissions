class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        time = 0
        queue = deque()

        rows, cols = len(grid), len(grid[0])
        dirs = [(0,1), (1,0), (-1,0), (0,-1)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r,c))

        while queue:
            n = len(queue)
            change = False

            for i in range(n):
                r,c = queue.popleft()

                for dr,dc in dirs:
                    nr, nc = r+dr, c+dc

                    if 0<= nr <rows and 0<= nc <cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        queue.append((nr,nc))
                        change = True

            # print(grid)
            # print(queue)
            time +=1 if change == True else 0 


        fresh = sum(1 for r in range(rows) for c in range(cols) if grid[r][c] == 1 )

        return time if fresh==0 else -1

        