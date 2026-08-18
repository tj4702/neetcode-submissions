class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        n = len(s)
        dp = [False] * (n+1)

        dp[0] = True

        for i in range(n):
            for j in range(i, n+1):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
                    # print(s[i:j])
                    # print(i,j)

        # print(dp)
        return dp[-1]



        