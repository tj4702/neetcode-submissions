# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        dummy = ListNode(0)
        heap = []
        curr = dummy 

        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        
        while heap:
            val, idx, node = heapq.heappop(heap)
            curr.next = ListNode(val)
            curr = curr.next
            curr.val = val

            if node.next:
                node = node.next 
                val = node.val
                heapq.heappush(heap, (val, idx, node))

        return dummy.next 




       