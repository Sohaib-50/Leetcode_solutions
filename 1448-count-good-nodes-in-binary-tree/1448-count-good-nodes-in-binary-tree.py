# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        def dfs(root, max_val_sofar):

            if not root:
                return 0

            if root.val >= max_val_sofar:
                max_val_sofar = root.val
                return 1 + dfs(root.left, max_val_sofar) + dfs(root.right, max_val_sofar)
            else:
                return dfs(root.left, max_val_sofar) + dfs(root.right, max_val_sofar)

        if root is None: return 0

        return 1 + dfs(root.left, root.val) + dfs(root.right, root.val)
        
