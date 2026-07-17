class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])
        stack = deque()
        minutes = 0 
        dirs = [(0,1),(1,0), (-1,0), (0,-1)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    stack.append((r,c))

        while stack:
            l_stack = len(stack)
            rot = False

            for i in range(l_stack):
                curr_r, curr_c = stack.popleft()

                for dr, dc in dirs:
                    nr, nc = curr_r + dr, curr_c +dc

                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        stack.append((nr, nc))
                        grid[nr][nc] = 2
                        rot = True
            minutes +=1 if rot else 0 

        return minutes if sum(1 for r in range(rows) for c in range(cols) if grid[r][c] == 1)== 0 else -1



