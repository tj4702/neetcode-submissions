class Solution:
    def minWindow(self, s: str, t: str) -> str:

        from collections import Counter 

        count_t = Counter(t)
        # print(count_t)
        count_s = defaultdict(int)
        l = 0
        have, need = 0 , len(count_t)
        res, res_len = '', float('inf')

        for r in range(len(s)):
            c = s[r]
            count_s[c] +=1

            if c in count_t and count_t[c] == count_s[c]:
                have +=1


            while have == need:
                if (r-l+1) < res_len:
                    res = s[l:r+1]
                    res_len = r-l +1

                count_s[s[l]] -=1

                if s[l] in count_t and count_s[s[l]] < count_t[s[l]]:
                    have -=1

                l +=1


        return res
        