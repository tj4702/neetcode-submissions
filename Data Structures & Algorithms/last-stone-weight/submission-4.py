from _heapq import heapify
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap = [-s for s in stones]
        heapq.heapify(heap)

        print(heap)

        while len(heap) > 1:
            print(heap)
            x1 = heapq.heappop(heap)
            x2 = heapq.heappop(heap)
            x1, x2 = -x1, -x2

            print(x1, x2)

            if x1 == x2:
                continue
            
            else:
                newstone = x1 - x2
                print(newstone)
                heapq.heappush(heap, -newstone)

        print(heap)

        return -heap[0] if heap else 0 
            


        