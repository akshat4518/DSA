# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        Q =[[root,0]]
        total= 0
        while Q:
            node , k =Q.pop(0)
            k=k*10+node.val
            if not node.left and not node.right:
                total=total+k
            if node.left:
                Q.append((node.left,k))
            if node.right:
                Q.append((node.right,k))
        return total