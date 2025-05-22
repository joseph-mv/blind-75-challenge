from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        Checks whether one tree is a subtree of another.

        Args:
            root : Root of the main tree.
            subRoot : Root of the potential subtree.

        Returns:
            True if subRoot is a subtree of root, False otherwise.
        """

        def same_tree(node1: Optional[TreeNode], node2: Optional[TreeNode]):
            if not node1 and not node2:
                return True

            if node1 and node2 and node1.val == node2.val:
                left = same_tree(node1.left, node2.left)
                right = same_tree(node1.right, node2.right)
                return left and right

            return False

        q = [root]
        while q:
            curr = q.pop(0)
            if same_tree(curr, subRoot):
                return True
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        return False
