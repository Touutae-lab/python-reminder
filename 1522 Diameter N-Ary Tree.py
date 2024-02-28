from math import inf


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
        
class Solution:
    def diameter(self, root: 'Node') -> int:
        if root == None:
            return 
        self.maxDiameter = 0

        def dfs(node):
            if node == None:
                return 0
            
            maxdepth = 0
            secondmaxdepth = 0
            
            
            for child in node.children:
                depth = dfs(child)
                if depth > maxdepth:
                    secondmaxdepth = maxdepth
                    maxdepth = depth
                elif depth > secondmaxdepth:
                    secondmaxdepth = depth
            self.maxDiameter = max(self.maxDiameter, maxdepth + secondmaxdepth)
            return maxdepth + 1
        dfs(root)
        return self.maxDiameter