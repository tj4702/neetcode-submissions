class Solution:
    def isPalindrome(self, s: str) -> bool:

        sen = [char.lower() for char in s if char.isalnum()]
        w = ''.join(sen)
        
        l, r = 0, len(w)-1

        while l<=r:
            if w[l] ==w[r]:
                r-=1
                l+=1
            else:
                return False
        return True