class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        n = len(nums)

        def backtrack(curr_path, visited):

            if len(curr_path)== n:
                res.append(curr_path[:])
                return 

            for j in range(n):
                if not visited[j]:
                    curr_path.append(nums[j])
                    visited[j] = not visited[j]
                    backtrack(curr_path, visited)
                    curr_path.pop()
                    visited[j] = not visited[j]


        visited = [False] * n

        backtrack([], visited)

        return res
            

        