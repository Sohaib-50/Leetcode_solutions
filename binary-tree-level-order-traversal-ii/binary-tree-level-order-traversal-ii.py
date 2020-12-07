# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return None
        
        from queue import Queue
        q = Queue()
        q.put(root)
        answer = []
        while not q.empty():
            current_level = []
            l = q.qsize()
            for _ in range(l):
                current_node = q.get()
                current_level.append(current_node.val)
                if current_node.left:
                    q.put(current_node.left)
                if current_node.right:
                    q.put(current_node.right)
                    
            answer.insert(0, current_level)
            
        return answer
                
            
