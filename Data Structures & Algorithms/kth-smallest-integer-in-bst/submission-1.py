# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        res = []
        found = False

        def dfs(node):
            nonlocal found
            if not node or found:
                return 
            
            dfs(node.left)

            if found:
                return 
            res.append(node.val)
           

            if len(res) ==k :
                found = True
                return 

            dfs(node.right)

            
        dfs(root)

        return res[k-1]

            
        