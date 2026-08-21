class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        combined = [(position[i], speed[i]) for i in range(len(speed))]
        combined.sort(key = lambda x: -x[0])
        time = []

        for x,y in combined:
            curr_time = (target - x)/y
            time.append(curr_time)

        stack = []


        for x in time :
            if not stack or x > stack[-1]:
                stack.append(x)

        return len(stack)
