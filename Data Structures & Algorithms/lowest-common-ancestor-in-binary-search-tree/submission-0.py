# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# BST is a tree where on the left all the nodes have a value less that the parent node and to the right is greater than the parent node and each node can have 2 or 0 nodes

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        
        while root:

            if max(p.val, q.val) < root.val:
                root = root.left
            
            elif min(p.val , q.val) > root.val:
                root = root.right
            
            else:
                return root