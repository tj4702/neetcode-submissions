# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res = []

        def helper(node):
            if not node:
                res.append('null')
                return 
            res.append(str(node.val))
            helper(node.left)
            helper(node.right)
        
        helper(root)
        return ','.join(res)

    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:

        tokens = iter(data.split(','))

        def helper():
            val = next(tokens)
            if val == 'null':
                return None
            node = TreeNode(int(val))
            node.left = helper()
            node.right = helper()

            return node

        return helper()











