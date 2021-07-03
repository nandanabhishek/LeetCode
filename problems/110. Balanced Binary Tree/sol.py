# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        
        # function to find height of binary tree
        def height(root):

            # base condition when binary tree is empty
            if root is None:
                return 0
            return max(height(root.left), height(root.right)) + 1
        
        # Base condition
        if root is None:
            return True

        # for left and right subtree height
        lh = height(root.left)
        rh = height(root.right)

        # allowed values for (lh - rh) are 1, -1, 0
        if (abs(lh - rh) <= 1) and self.isBalanced(
        root.left) is True and self.isBalanced( root.right) is True:
            return True

        # if we reach here means tree is not
        # height-balanced tree
        return False
