class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        tot_gas = sum(gas)
        tot_cost = sum(cost)

        if tot_cost > tot_gas:
            return - 1

        n = len(cost)
        tot = 0 
        res = 0 
        
        for i in range(n):
            tot += gas[i] - cost[i]

            if tot < 0 :
                tot = 0 
                res = i + 1
        
        return res

