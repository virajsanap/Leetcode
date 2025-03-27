# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def check(rl,rr):
            if not rl or not rr or rl.val!=rr.val:
                return rl is None and rr is None

            return (check(rl.left,rr.right) and check(rl.right, rr.left))
        return check(root.left, root.right)
            
