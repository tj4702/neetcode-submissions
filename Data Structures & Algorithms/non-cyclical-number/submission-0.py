class Solution:
    def isHappy(self, n: int) -> bool:

        seen = set()
        i = 0 

        while i < 100 and n != 1:

            res = 0
            temp = n

            while temp //10 != 0 :
                quo = (temp//10)
                rem = (temp%10)
                res += (rem) ** 2
                temp = quo
            
            res += (temp) ** 2
            n = res

            if n in seen:
                return False
            
            seen.add(n)
            print(seen)
            print(n)

        return n==1

        