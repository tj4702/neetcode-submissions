class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        rows, cols = len(matrix), len(matrix[0])

        low_r, high_r = 0,rows
        low_c, high_c = 0, cols

        while low_r < high_r:
            mid = (low_r+ high_r)//2
            curr = matrix[mid]
            min_val, max_val = curr[0], curr[-1]

            if target > max_val:
                low_r = mid +1
            elif target < min_val:
                high_r = mid
            
            else:
                break

        mid_r = mid

        while low_c < high_c:
            mid = (low_c+ high_c)//2
            curr = matrix[mid_r][mid]

            if target > curr:
                low_c = mid +1
            elif target < curr:
                high_c = mid
            
            elif curr == target:
                return True

        return False
