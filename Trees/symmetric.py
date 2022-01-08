# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isMirror(self, leftnode, rightnode):
        if (leftnode and rightnode):
            return leftnode.val == rightnode.val and self.isMirror(leftnode.left, rightnode.right) and self.isMirror(leftnode.right, rightnode.left)
        return leftnode == rightnode
        
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        return self.isMirror(root.left, root.right)