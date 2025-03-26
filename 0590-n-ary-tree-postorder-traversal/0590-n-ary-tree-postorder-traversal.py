"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res=[]
        def posto(root):
            if not root:
                return
            for i in root.children:
                posto(i)
            res.append(root.val)
            
        posto(root)
        return res