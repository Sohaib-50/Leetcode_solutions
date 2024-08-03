# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        '''
        ## THOUGHT PROCESS ##
        Need a way to find leaf sequences of binary trees.
        I think we will need to find them separately and cant find em together for both trees

        To find leaf sequence what can be done?
        Idea 0:
            Do DFS, always preferring left side. Mantain a sequence list
            Add to list whenever leaf node found.   
            After finding leaf sequence for both trees, just compare em!

        Lets implement.
        '''

        def leaf_value_sequence(root: Optional[TreeNode], sequence_sofar=[]):
            if root is None:
                return

            # leaf node
            if (root.left is None) and (root.right is None):
                sequence_sofar.append(root.val)
                return

            # DFS
            leaf_value_sequence(root.left, sequence_sofar)
            leaf_value_sequence(root.right, sequence_sofar)

        root1_leaf_value_sequence = []
        leaf_value_sequence(root1, root1_leaf_value_sequence)

        root2_leaf_value_sequence = []
        leaf_value_sequence(root2, root2_leaf_value_sequence)

        # print(root1_leaf_value_sequence, root2_leaf_value_sequence)

        return root1_leaf_value_sequence == root2_leaf_value_sequence
