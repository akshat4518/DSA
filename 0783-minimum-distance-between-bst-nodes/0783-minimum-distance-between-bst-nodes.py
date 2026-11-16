class Solution:
    def minDiffInBST(self, root: TreeNode | None) -> int:
        prev = None
        min_distance = float('inf')

        def inorder(node):
            nonlocal prev , min_distance

            if node is None:
                return 
            
            inorder(node.left)

            if prev is not None:
                distance = node.val - prev
                min_distance = min(min_distance, distance)

            prev = node.val

            inorder(node.right)

        inorder(root)
        return min_distance