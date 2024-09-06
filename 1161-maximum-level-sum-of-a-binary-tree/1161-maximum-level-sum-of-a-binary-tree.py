# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:

        max_sum_level = 0
        max_sum = float('-inf')
        queue = [root]
        level = 1
        while queue:

            level_sum = 0

            for level_size in range(len(queue)):
                current = queue.pop(0)
                level_sum += current.val
                
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)

            if level_sum > max_sum:
                max_sum = level_sum
                max_sum_level = level

            level += 1
        
        return max_sum_level


        
