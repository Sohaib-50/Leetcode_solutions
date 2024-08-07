# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:


        def dfs(node, path_sum, path_sum_history):

            if not node:
                return 0
            
            path_sum += node.val

            required = path_sum - targetSum
            count = path_sum_history.get(required, 0)

            path_sum_history[path_sum] = path_sum_history.get(path_sum, 0) + 1

            count += dfs(node.left, path_sum, path_sum_history)
            count += dfs(node.right, path_sum, path_sum_history)

            path_sum_history[path_sum] -= 1

            return count
            

        return dfs(root, 0, {0: 1})
        
