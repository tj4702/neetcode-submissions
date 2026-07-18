class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []

        def backtrack(curr_path, sp, ep):

            if sp == n and ep == n:
                req = ''.join(curr_path[:])
                res.append(req)
                return 
            
            if sp < n:
                curr_path.append('(')
                backtrack(curr_path, sp+1, ep)
                curr_path.pop()
            
            if ep < sp:
                curr_path.append(')')
                backtrack(curr_path, sp, ep+1)
                curr_path.pop()

        
        backtrack([] , 0, 0)

        return res
            




