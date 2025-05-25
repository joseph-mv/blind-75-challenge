from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        Determine if it is a valid binary search tree (BST).
        Args:
            root: Root of binary tree.
        Returns:
            True if the tree is a valid BST, otherwise False.
        """

        def validate(root, max_val, min_val):
            if not root:
                return True

            if min_val < root.val < max_val:
                left = validate(root.left, root.val, min_val)
                right = validate(root.right, max_val, root.val)
                return left and right

            return False

        return validate(root, float("inf"), float("-inf"))
