# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: TreeNode | None) -> int:
        c=0
        def find(node):
            nonlocal c
            if not node:
                return -1
            left = find(node.left)
            right=find(node.right)
            if left==0 or right ==0:
                c=c+1
                return 1
            if left==1 or right==1:
                return -1
            return 0
        if find(root)==0:
            c=c+1
        return c
