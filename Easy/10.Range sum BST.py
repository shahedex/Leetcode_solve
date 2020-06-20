# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        st = []
        sum = 0
        while True:
            if root:
                st.append(root)
                root = root.left
            else:
                if len(st) < 1:
                    break
                popped = st.pop()
                if L <= popped.val <= R:
                    sum += popped.val
                root = popped.right
        return sum
