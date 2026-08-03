class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []

        for x,y in points:
            dist = (x**2 + y ** 2)**0.5
            heap.append((-dist,x,y))

        heapq.heapify(heap)

        while len(heap) > k:
            heapq.heappop(heap)

        # print(heap)

        res = [[x,y] for dist, x,y in heap]

        return res



        