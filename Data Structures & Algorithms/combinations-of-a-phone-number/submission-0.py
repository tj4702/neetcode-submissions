class Solution:
    def letterCombinations(self, digits: str) -> List[str]:


        mapping = { '2' : 'abc', '3' :'def', '4':'ghi', '5': 'jkl', '6': 'mno', 
                    '7': 'pqrs', '8':'tuv', '9':'wxyz'}
        
        res = []
        n = len(digits)

        if not digits:
            return []

        def backtrack(path, i):
            if i == n:
                curr = ''.join(path[:])
                res.append(curr)
                return 

            for x in mapping[digits[i]]:
                path.append(x)
                backtrack(path, i+1)
                path.pop()
        
        backtrack([], 0)

        return res 