class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        

        s = len(s1)
        t = len(s2)

        left = 0 

        for right in range(t-s+1):
            curr = s2[right : right + s]

            if sorted(s1) == sorted(curr):
                return True

        return False