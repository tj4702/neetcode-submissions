class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        res = 0 
        n = len(digits)
        digits = digits[::-1]


        for i in range(n):
            res += (10 ** i) * digits[i]
            print(res)

        res += 1
        # print(res)

        res = [int(x) for x in list(str(res))]
        # print(res)

        return res
        