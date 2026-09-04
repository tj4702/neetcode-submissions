class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        cost = [float('inf')] * n 
        cost[src] = 0

        for i in range(k+1):
            temp = cost.copy()

            for u,v , w in flights:
                if cost[u]+w < temp[v]:
                    temp[v] = cost[u] + w 
            
            cost = temp

        return cost[dst] if cost[dst] != float('inf') else - 1
        
        