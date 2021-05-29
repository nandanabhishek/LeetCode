# Approach - 1: Simple Iterative approach



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        temp=root
        while temp:
            if temp.val==val: 
                return temp
            if temp.val<val:
                temp=temp.right
            else:
                temp=temp.left
        return None
        
        
        
        
        
        
        
# Approach - 2: Recursive Approach




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root:
            if root.val==val:
                return root
            if root.val>val:
                return self.searchBST(root.left, val)
            else:
                return self.searchBST(root.right, val)
        return None
                
            
            
        
        
