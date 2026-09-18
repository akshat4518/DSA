class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node, path, result):
            if not node:
                return
            path.append(str(node.val))
            if not node.left and not node.right:
                result.append('->'.join(path))
            else:
                dfs(node.left, path, result)
                dfs(node.right, path, result)
            path.pop()  # Backtrack by removing the last element

        result = []
        dfs(root, [], result)
        return result