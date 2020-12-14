# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        from collections import deque
        
        queue = deque()
        queue.append(root)
        result = []
        while queue:
            level_size = len(queue)
            level_sum = 0
            for _ in range(level_size):
                current_node = queue.popleft()
                level_sum += current_node.val
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
            result.append(level_sum / level_size)
            
        return result
