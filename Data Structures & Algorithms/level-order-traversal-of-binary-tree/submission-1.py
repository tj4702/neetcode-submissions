# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = defaultdict(list)

        def dfs(node, depth):
            
            if not node:
                return None
            
            res[depth].append(node.val)
            
            if node.left:
                dfs(node.left, depth+1)
            
            if node.right:
                dfs(node.right, depth+1)

        
        dfs(root, 0 )
        res = [v for v in res.values()]
        return res



        