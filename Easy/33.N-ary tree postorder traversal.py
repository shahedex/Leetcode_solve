"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        st = []
        ret = []
        if not root:
            return ret
        st.append(root)
        while len(st) > 0:
            popped = st.pop()
            ret.append(popped.val)
            for child in popped.children:
                st.append(child)
        return reversed(ret)
