class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = [c.lower() for c in s if c.isalnum()]

        s = ''.join(s)

        return s == s[::-1]