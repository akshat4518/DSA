# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode | None) -> int:
        Q =[root]
        while Q:
            node=Q.pop(0)
            if node.right:
                Q.append(node.right)
            if node.left:
                Q.append(node.left)
        return node.val
        