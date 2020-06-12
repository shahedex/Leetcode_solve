# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return
        q = deque()
        q.append(root)
        ret = []
        while len(q) > 0:
            dum = []
            c = len(q)
            while c > 0:
                popped = q.popleft()
                dum.append(popped.val)
                if popped.left:
                    q.append(popped.left)
                if popped.right:
                    q.append(popped.right)
                c -= 1
            ret.append(dum)
        return ret
