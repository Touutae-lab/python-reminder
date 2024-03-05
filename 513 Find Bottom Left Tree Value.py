# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Deque


class Solution:
    def findBottomLeftValue(self, root):
        dfs = Deque()
        dfs.append(root)
        left_most = root
        while dfs:
            left_most = dfs[0]
            for i in range(len(dfs)):
                item = dfs.popleft()
                if item.left: dfs.append(item.left)
                if item.right: dfs.append(item.right)
        return left_most.val