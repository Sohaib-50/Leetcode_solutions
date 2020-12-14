"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
​
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        from collections import deque
        
        result = []
        if not root:
            return result
        
        queue = deque()
        queue.append(root)
        while queue:
            level_size = len(queue)
            current_level = []
​
            for _ in range(level_size):
                current_node = queue.popleft()
                current_level.append(current_node.val)
                for child in current_node.children:
                    queue.append(child)
                
            result.append(current_level)        
        
        return result        
        
