class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        mapping = {
            '2': 'abc', 
            '3': 'def', 
            '4':'ghi', 
            '5':'jkl', 
            '6':'mno', 
            '7':'pqrs',
            '8': 'tuv', 
            '9':'wxyz'
        }

        n = len(digits)

        res = []

        if not digits:
            return []

        def backtrack(curr, i):

            if i == n:
                req = ''.join(curr[:])
                res.append(req)
                return 

            for letter in mapping[digits[i]]:
                curr.append(letter)
                backtrack(curr, i+1)
                curr.pop()

        
        backtrack([], 0)

        return res


        
















