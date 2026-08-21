class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        combined = [(position[i], speed[i]) for i in range(len(speed))]
        combined.sort(key = lambda x: -x[0])
        time = []

        for x,y in combined:
            curr_time = (target - x)/y
            time.append(curr_time)

        # target is the position we want to be at and if we reach at the same time like the number of postions for the finish line I think 
        # so here what we do is target - position is the diff in the distance to be travelled so if any two cars meet each other at any given checkpoint they merge so to check that exact thing we speed = distance/ time and distance = target - position and then what we do is that we get the time from this when two cars merge ?
        # so if any two cars are the same time away from the target we merge them togther as one 
        
        stack = []

        for x in time :
            if not stack or x > stack[-1]:
                stack.append(x)

        return len(stack)
