class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        # kth largest elemnt means that we pop for len(nums) - k+1 times and we need to do like the maxheap which is just -n for minheap

        nums = [-n for n in nums]

        n = len(nums)

        heapq.heapify(nums)
        # print(nums)

        if n < k:
            return -1

        for _ in range(k-1):
            heapq.heappop(nums)
            # print(nums)

        return -1 * nums[0] if nums else -1

        