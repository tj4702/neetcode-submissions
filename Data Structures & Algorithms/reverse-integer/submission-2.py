class Solution:
    def reverse(self, x: int) -> int:

        res = 0 
        neg = -1 if x < 0 else 1
        x = abs(x)

        while x //10 != 0 :
            digit = x % 10 
            x = x //10 
            res = res  * 10 + digit
        
        res = res * 10 + x%10


        return (res * neg) if res in range(-2**31, 2 ** 31) else 0 
        