# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def BST(node, max_val , min_val):
            if not node:
                return True

            if not(node.val >  min_val and node.val < max_val):
                return False

            left_tree = BST(node.left, node.val , min_val)
            right_tree = BST(node.right, max_val  , node.val)

            return left_tree and right_tree

        return BST(root, float('inf'), float('-inf'))


        