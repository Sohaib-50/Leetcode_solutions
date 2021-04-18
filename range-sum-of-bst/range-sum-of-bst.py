# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        if root is None:
            return 0
        if root.val in range(low, high + 1):
            ans = root.val
        else:
            ans = 0
            
        return ans + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)