# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        s = []
        res = []
        while True:
            if root != None:
                s.append(root)
                root = root.left
            else:
                if len(s) < 1:
                    break
                popped = s.pop()
                res.append(popped.val)
                root = popped.right
        return res
