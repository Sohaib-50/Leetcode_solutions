# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # queue = []
        # queue.append(root)
        # current_level_size = 1
        # leaf_reached =
        # while queue:
        #     current_level_size = len(queue)
        #     for _ in range(current_level_size):
        #         current_node = queue.pop()
        if root is None:
            return True
        if root.left is None:
            if root.right:
                return root.right.left == root.right.right == None
            return True
        if root.right is None:
            return root.left.left == root.left.right == None
        
        stack = [root]
        while stack:
            current = stack.pop()
            if current.left:
                left_height = Solution.height(current.left)
                stack.append(current.left)
            else:
                left_height = 0
    
            if current.right:
                right_height = Solution.height(current.right)
                stack.append(current.right)
            else:
                right_height = 0
                
            if abs(left_height - right_height) > 1:
                return False
            
        return True
    
        # print((Solution.height(root.left), Solution.height(root.right)))
        # return abs((Solution.height(root.left) - Solution.height(root.right))) <= 1
    
    @staticmethod
    def height(root: TreeNode) -> int:
        if root.right is None and root.left is None:
            return 1
        rh = 0
        lh = 0
        if root.right is not None:
            rh = Solution.height(root.right)
        if root.left is not None:
            lh = Solution.height(root.left)
        return max(rh, lh) + 1
        # if node.left == node.right == None:
        #     return 1
        # print(node.val)
        # return max(Solution.height(node.left), Solution.height(node.right))
        