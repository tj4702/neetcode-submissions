class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)
        dp = [[False] * n for _ in range(n)]
        max_len = 0 
        ans = ''

        for i in range(n):
            dp[i][i] = True
            ans = s[i]
        
        for i in range(n-1, -1, -1):
            for j in range(i + 1, n):

                if s[i] == s[j] and (j - i == 1 or dp[i+1][j-1]):
                    dp[i][j] = True
                    if j-i +1 > max_len:
                        max_len = j-i +1
                        ans = s[i:j+1]
        

        return ans