# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], min_val=float('-inf'), max_val=float('inf')) -> bool:
        if not (min_val < root.val < max_val):
            return False

        right_valid = left_valid = True

        if root.right:
            right_valid = self.isValidBST(root.right, root.val, max_val)

        if root.left:
            left_valid = self.isValidBST(root.left, min_val, root.val)

        return right_valid and left_valid
