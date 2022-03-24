# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, lower_limit, upper_limit) -> bool:
            if not root:
                return True
            
            if not (lower_limit < root.val < upper_limit):
                return False
            
            return helper(root.left, lower_limit, root.val) and helper(root.right, root.val, upper_limit)
                
            
        
        return helper(root, float('-inf'), float('inf'))