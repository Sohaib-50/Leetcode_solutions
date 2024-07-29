# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def depth(root, depth_sofar=0):
            if not root:
                return depth_sofar

            depth_sofar += 1

            return max(depth(root.left, depth_sofar), depth(root.right, depth_sofar))

        return depth(root)
