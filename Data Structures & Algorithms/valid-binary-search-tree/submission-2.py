# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, maxVal, minVal):

            if not node:
                return True

            if not(minVal < node.val < maxVal):
                return False
            
            left_subtree = dfs(node.left, node.val, minVal)
            right_subtree = dfs(node.right, maxVal, node.val)

            return left_subtree and right_subtree

        return dfs(root, float('inf'), float('-inf'))



        
        