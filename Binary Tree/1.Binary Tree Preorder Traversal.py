# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        st = []
        ret = []
        st.append(root)
        while len(st) != 0:
            popped = st.pop()
            if popped != None:
                ret.append(popped.val)
                st.append(popped.right)
                st.append(popped.left)
        return ret
