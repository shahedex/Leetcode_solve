# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return root is None or self.check(root.left, root.right)
    def check(self, lroot, rroot):
        if not lroot and not rroot:
            return True
        elif lroot and rroot:
            return lroot.val == rroot.val and self.check(lroot.left, rroot.right) and self.check(lroot.right, rroot.left)
        return False
