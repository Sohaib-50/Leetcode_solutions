# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    '''
    At every node, all nodes on the left (anywhere down the line) MUST be smaller,
    and all nodes on the right must be greater. Basic BST law.

    We’ve decided to delete `k` by replacing it with `l` (the left subtree).
    Now we’re left with `r` (the right subtree) hanging.

    At first I thought maybe we’d have to dig into both subtrees and
    manipulate all their children. Turns out: nope.

    Since `r` was to the right of `k`, and `l` was to the left,
    every value in `r` is guaranteed to be greater than every value in `l`.

    So our goal is just to plug `r` *somewhere* into `l` in a way that keeps the order valid.

    And that "somewhere" is simple:
    Go to the rightmost node in `l` — because everything in `r` is bigger than that.
    We don’t even need to look at the left side at all.

    Just move right-right-right until there's no more right — then slam `r` in there.
    That’s our safe insertion point.
    '''
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        if not root:
            return root

        # key in subtree
        if root.val != key:
            # delete in right subtree case
            if root.val < key:
                root.right = self.deleteNode(root.right, key)
            
            # delete in left subtree case
            else:
                root.left = self.deleteNode(root.left, key)
            
            return root

        ## --deletion case--
        left_subtree = root.left
        right_subtree = root.right
        if not left_subtree:
            return right_subtree

        # perform deletion by replacing the key node with its left subtree
        root = left_subtree

        # add right_subtree back while preserving order
        '''
        All values in right_subtree would be greater than that of left_subtree,
        due to the fact that left was left of key and right was right of key,
        hence the only place to attatch right_subtree would be at the
        right-most position of left_subtre
        '''
        while left_subtree.right:
            left_subtree = left_subtree.right
            
        left_subtree.right = right_subtree

        return root

        
            
