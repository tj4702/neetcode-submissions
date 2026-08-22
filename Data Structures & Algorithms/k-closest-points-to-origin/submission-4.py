class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []

        for i in range(len(points)):
            x,y = points[i]
            dist = (x**2 + y **2) ** 0.5
            heapq.heappush(heap, [-dist, x, y])

            if len(heap)>k:
                heapq.heappop(heap)

        # print(heap)

        res = [(x,y) for dist, x, y in heap[:k]]

        return res
        