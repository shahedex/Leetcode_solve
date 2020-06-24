# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return
        found = False
        st = []
        st.append(root)
        while len(st) > 0:
            popped = st.pop()
            if popped.val == val:
                root = popped
                found = True
                break
            if popped.right:
                st.append(popped.right)
            if popped.left:
                st.append(popped.left)
        if not found:
            return 
        return root
