class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        n = len(points)
        graph = [[0] * n for _ in range(n)]

        for i in range(n):
            x1,y1 = points[i]
            for j in range(i, n):
                x2,y2 = points[j]
                dist = abs(x1- x2) + abs(y1-y2)
                graph[i][j] = dist
                graph[j][i] = dist

        heap = [(0,0)]      # 0th node and 0 cost so far 
        visited = set()
        total_cost = 0 

        while heap and len(visited) < n :
            cost, node = heapq.heappop(heap)

            if node in visited:
                continue
            
            visited.add(node)
            total_cost += cost
            for nei in range(n):
                if nei not in visited:
                    heapq.heappush(heap, (graph[node][nei], nei))




        return total_cost
        