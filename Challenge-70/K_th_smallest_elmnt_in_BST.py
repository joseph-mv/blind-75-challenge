# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root:TreeNode, k: int) -> int:
        """
        Find out K_th smallest element in a BST
        Args:
            root: Root of a binary search tree
            k (int): The 1-indexed position of the smallest element to find.

        Returns:
            int: The kth smallest value in the BST.
        """
        count = 0
        value = root.val

        def dfs(root):
            nonlocal count, value
            if not root:
                return
            dfs(root.left)
            count += 1
            if count == k:
                value = root.val
            dfs(root.right)

        dfs(root)
        return value
