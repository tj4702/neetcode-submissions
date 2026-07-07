class Solution:
    def isPalindrome(self, s: str) -> bool:

        s = [x.lower() for x in s if x.isalnum()]
        s = ''.join(s)

        return s == s[::-1]