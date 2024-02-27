from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def dept(self, root: Optional[TreeNode]) -> int:
        if (root == None):
            return 0
        return max(self.dept(root.left), self.dept(root.right))  + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        def dfs(node: Optional[TreeNode]):
            if not node:
                return 0
            left = dfs(node.left) 
            right = dfs(node.right)
            self.result = max(self.result, left+right)
            return 1 + max(left, right)
        dfs(root)
        return self.result