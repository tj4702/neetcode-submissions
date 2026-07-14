class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        count = defaultdict(int)

        res = 0 

        left = 0 

        maxf = 0 
        n = len(s)


        for right in range(n):
            count[s[right]] +=1
            maxf = max(maxf, count[s[right]])
            
            while (right - left +1) - maxf > k :
                count[s[left]] -=1
                left +=1
            
            res = max(res, right - left +1)

        return res