class Solution:
    def isValid(self, s: str) -> bool:

        mapping = {
                    '{':'}', 
                    '(':')', 
                    '[':']'
                    }

        stack = []

        for char in s:
            if char in mapping:
                stack.append(char)
                continue
            
            if not stack:
                return False
            
            if mapping[stack[-1]] != char:
                return False
            
            stack.pop()
        
        return not stack
