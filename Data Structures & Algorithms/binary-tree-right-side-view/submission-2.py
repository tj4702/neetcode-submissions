# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        # bfs needs to be done here 

        stack = deque()

        if not root:
            return []

        stack.append(root)

        res = []

        while stack:
            n = len(stack)
            # print(f"n == {n}")


            for i in range(n):
                node = stack.popleft()
                if not node:
                    continue
                # print(node.val)
                if node.left:
                    # print(f'node.left is {node.left.val}')
                    stack.append(node.left)
                
                if node.right:
                    # print(f'node.right is {node.right.val}')
                    stack.append(node.right)

            res.append(node.val)

        return res

                






