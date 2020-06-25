"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        st = []
        ret = []
        if not root:
            return st
        st.append(root)
        while len(st) > 0:
            popped = st.pop()
            ret.append(popped.val)
            childs = popped.children
            childs.reverse()
            for child in childs:
                st.append(child)
            
        return ret
