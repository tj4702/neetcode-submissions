class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        n = len(nums)

        def backtrack(curr, visited):

            if len(curr) == n:
                res.append(curr[:])
                return 

            for j in range(n):
                if not visited[j]:
                    curr.append(nums[j])
                    visited[j] = not visited[j]
                    backtrack(curr, visited)
                    curr.pop()
                    visited[j] = not visited[j]
            
        
        visited = [False] * n

        backtrack([], visited)

        return res




            


        