# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: TreeNode | None) -> int:
        max_s=float('-inf')
        def bt(node):
            nonlocal max_s
            if not node :
                return 0
            left = max(bt(node.left),0)
            right =max(bt(node.right),0)
            Total =node.val+left+right
            max_s =max(Total,max_s)
            return node.val+max(left,right)
        bt(root)
        return max_s