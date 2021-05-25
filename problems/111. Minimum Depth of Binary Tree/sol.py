# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if root.left==None or root.right==None:
            return 1+self.minDepth(root.left)+self.minDepth(root.right)
        
        return 1+min(self.minDepth(root.right),self.minDepth(root.left))
        
