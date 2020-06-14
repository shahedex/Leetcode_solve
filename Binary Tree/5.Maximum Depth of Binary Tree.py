# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    ans = 0
    
    def maxDepth(self, root: TreeNode) -> int:
        self.getDepth(root, 1)
        return self.ans
    
    def getDepth(self, root, val):
        if not root:
            return
        if not root.left and not root.right:
            self.ans = max(self.ans, val)
        self.getDepth(root.left, val + 1)
        self.getDepth(root.right, val + 1)
