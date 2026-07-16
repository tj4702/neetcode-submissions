class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        rows, cols = len(matrix), len(matrix[0])

        mapping_row = defaultdict(bool)
        mapping_col = defaultdict(bool)

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0 :
                    mapping_row[r] = True
                    mapping_col[c] = True

        for r in range(rows):
            if mapping_row[r]:
                matrix[r] = [0] * cols

                
        
        for c in range(cols):
            if mapping_col[c]:
                for r in range(rows):
                    matrix[r][c] = 0
