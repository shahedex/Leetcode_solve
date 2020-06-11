# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        s1 = []
        s2 = []
        if not root:
            return s1
        s1.append(root)
        while len(s1) > 0:
            popped = s1.pop()
            if popped.left is not None:
                s1.append(popped.left)
            if popped.right is not None:
                s1.append(popped.right)
            s2.append(popped.val)
        return reversed(s2)
