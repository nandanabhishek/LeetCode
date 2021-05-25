# best approach : 



"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
            def DFS(root, ans):
                if root:                          # only continue when root is not None
                    ans.append(root.val)          # Append the root
                    for child in root.children:   # And recurse for its children
                        DFS(child, ans)
                return ans

            ans=[]
            return DFS(root, ans)





# Approach - 1 :



"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        output =[]
        
        # perform dfs on the root and get the output stack
        self.dfs(root, output)
        
        # return the output of all the nodes.
        return output
    
    
    def dfs(self, root, output):
        
        # If root is none return 
        if root is None:
            return
        
        # for preorder we first add the root val
        output.append(root.val)
        
        # Then add all the children to the output
        for child in root.children:
            self.dfs(child, output)
            
            
            
            
            
            
            
            
            
 # Approach - 2 :



"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        def DFS(root):
            if root:
                out.append(root.val)
                for child in root.children:
                    DFS(child)

        out = []
        DFS(root)

        return out
        
        
