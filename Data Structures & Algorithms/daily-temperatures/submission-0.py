class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []
        
        stack.append(0)
        n = len(temperatures)
        res = [0] * n

        for i in range(1,len(temperatures)):
            while stack:
                prev = stack.pop()
                if temperatures[prev] < temperatures[i]:
                    res[prev] = i - prev 
                else:
                    stack.append(prev)
                    break
            stack.append(i)
            
        #     print(stack)
        # print(res)

        return res 




        