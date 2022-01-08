# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        hashset = set()
        # BST
        # q = deque([root])
        # while q:
        #     node = q.popleft()
        #     target = k - node.val
        #     if target in hashset:
        #         return True
        #     else:
        #         hashset.add(node.val)
        #     if node.left:
        #         q.append(node.left)
        #     if node.right:
        #         q.append(node.right)
        # return False

        # DFS
        def dfs(node):
            if not node: return False
            target = k - node.val
            if target in hashset:
                return True
            else:
                hashset.add(node.val)
            return dfs(node.left) or dfs(node.right)
        return dfs(root)