# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:

        def zigzagdfs(node, prev_direction, len_sofar):

            if prev_direction == "left":
                right_path_len = zigzagdfs(node.right, "right", len_sofar + 1) if node.right else len_sofar
                left_path_len = zigzagdfs(node.left, "left", 1) if node.left else len_sofar
            else:
                right_path_len = zigzagdfs(node.right, "right", 1) if node.right else len_sofar
                left_path_len = zigzagdfs(node.left, "left", len_sofar + 1) if node.left else len_sofar

            return max(right_path_len, left_path_len)

        return max(
            zigzagdfs(node=root, prev_direction='left', len_sofar=0),
            zigzagdfs(node=root, prev_direction='right', len_sofar=0)
        )
        
