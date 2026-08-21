class Solution:
    def isValid(self, s: str) -> bool:

        mapping = {
            '{': '}', 
            '(':')', 
            '[': ']'
        }

        stack = []


        for c in s:
            if c in mapping:
                stack.append(c)
                continue
        
            if stack and mapping[stack[-1]] == c:
                stack.pop()
                continue
            else:
                return False

        return not stack
        