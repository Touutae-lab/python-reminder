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
        if (root == None):
            return 0
        
        lHeight = self.dept(root.left)
        rHeight = self.dept(root.right)

        lDiameter = self.diameterOfBinaryTree(root.left)
        rDiameter = self.diameterOfBinaryTree(root.right)

        return max(lHeight + rHeight, max(lDiameter, rDiameter))