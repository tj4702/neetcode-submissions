class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:

        n = len(matrix)

        # start with trying to do this in a new 2D matrix

        grid = matrix
        extra = 0 

        for r in range(n//2 ):
            row1, row2 = grid[r], grid[n-r-1]
            grid[r] = row2
            grid[n-r-1] = row1
        

        for r in range(n):
            for c in range(r+1, n):
                grid[r][c], grid[c][r] = grid[c][r], grid[r][c]
                # print(grid)

        