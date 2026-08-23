# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        good = 0

        def dfs(node, maxSoFar):

            nonlocal good

            if not node:
                return 

            if node.val >= maxSoFar:
                maxSoFar = node.val
                good +=1 
            
            if node.left:
                dfs(node.left, maxSoFar)
            
            if node.right:
                dfs(node.right, maxSoFar)

        dfs(root, float('-inf'))

        return good