class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        res = 0 
        n = len(digits)
        digits = digits[::-1]


        for i in range(n):
            res += (10 ** i) * digits[i]

        res += 1
        res = [int(x) for x in list(str(res))]

        return res
        