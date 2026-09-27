class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:

        heap = [(grid[0][0], 0, 0 )]
        m , n = len(grid), len(grid[0])

        heapq.heapify(heap)

        dirs = [(0,1), (1,0), (-1,0), (0,-1)]

        visited = set()

        visited.add((0,0))

        t = 0

        while heap:
            val, row, col = heapq.heappop(heap)
            t = max(t, val)

            if row == m-1 and col == n-1 :
                return t

            for dr, dc in dirs:
                nr, nc = row +dr, col +dc

                if 0 <= nr < m and 0<=nc<n and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    heapq.heappush(heap, (grid[nr][nc], nr, nc))

        return -1 







