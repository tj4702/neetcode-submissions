class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        res = []

        def backtrack(curr, sp, ep):
            if sp == n and ep == n:
                req = ''.join(curr[:])
                res.append(req)
                return 

            
            if sp < n:
                curr.append('(')
                backtrack(curr, sp+1, ep)
                curr.pop()

            if ep< sp:
                curr.append(')')
                backtrack(curr, sp, ep+1)
                curr.pop()

        backtrack([],0,0)

        return res
        
        