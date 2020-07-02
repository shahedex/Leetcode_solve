# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        st = []
        ret = []
        while True:
            if root:
                st.append(root)
                root = root.left
            else:
                if len(st) < 1:
                    break
                popped = st.pop()
                ret.append(popped.val)
                root = popped.right
        cur = ans = TreeNode()
        for val in ret:
            cur.right = TreeNode(val=val)
            cur = cur.right
        return ans.right
