class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        count = defaultdict(int)
        max_char = 0 
        res = 0 
        left= 0 
        n = len(s)
       
        for right in range(n):
            count[s[right]] += 1
            max_char = max(max_char, count[s[right]])

            while ((right - left +1 ) - max_char ) > k:
                count[s[left]] -= 1
                left +=1

            res = max(res, right - left +1)

        return res