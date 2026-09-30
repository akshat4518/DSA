# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def traverse(self, head):
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
        return arr
    
    def make_bst(self, inorder, low=0, high=None):
        if low > high:
            return None
        
        mid = (low + high) // 2
        
        root = TreeNode(inorder[mid])
        
        root.left = self.make_bst(inorder, low, mid - 1)
        root.right = self.make_bst(inorder, mid + 1, high)
        
        return root

    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        inorder = self.traverse(head)
        return self.make_bst(inorder, 0, len(inorder) - 1)