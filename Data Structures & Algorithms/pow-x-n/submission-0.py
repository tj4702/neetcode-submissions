class Solution:
    def myPow(self, x: float, n: int) -> float:

        res = 1

        if n < 0 :
            x = 1/x
            n = abs(n)

        for _ in range(n):
            res *= x
        
        return res
        