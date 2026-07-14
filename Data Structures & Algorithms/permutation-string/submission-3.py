class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        

        s = len(s1)
        t = len(s2)

        freq_s = [0] * 26
        freq_t = [0] * 26

        for char in s1:
            freq_s[ord(char) - ord('a')] +=1
        
        for char in s2[:s]:
            freq_t[ord(char)-ord('a')] +=1

        if freq_s == freq_t:
            return True

        left = 0 

        for right in range(s,t):
            freq_t[ord(s2[left]) - ord('a') ]-=1
            freq_t[ord(s2[right]) - ord('a')]+=1
            if freq_t == freq_s:
                return True
            left += 1

        return False
            
