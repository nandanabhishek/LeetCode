# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        # base case
        if root is None:
            return
        out = []  # to store result of level order traversal
        q = [root]
        while q:
            level = len(q)
            ans = []
            while level:
                node = q.pop(0)
                level -=1
                ans.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            out.append(ans)
        return out
    
    
    # This is BFS (Queue is used in its implementataion)
        
