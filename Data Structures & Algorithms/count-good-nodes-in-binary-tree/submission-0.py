# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:


        def good(node, maxnode):

            if not node:
                return 0

            is_good = 1 if node.val >= maxnode else 0 

            right_good = good(node.right, max(node.val, maxnode))
            left_good = good(node.left, max(node.val, maxnode)) 

            return is_good + right_good + left_good 


        
        return good(root, root.val)

            

        




        