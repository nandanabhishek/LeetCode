# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isSym(L,R):
            if  L==None and R==None: 
                return True
            if (L and R) and L.val == R.val: 
                return isSym(L.left, R.right) and isSym(L.right, R.left)
            
            return False
        
        # base case
        if not root:
            return True
        
        return isSym(root.left, root.right)
            
        
