# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base Cases
        if p is None:
            return q is None
        elif q is None:
            return False
        elif p.val != q.val:
            return False
        
        # recursive relation
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)