# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":
        """
        Find out Lowest Common Ancestor of a Binary Search Tree

        Args:
            root : The root of the binary search tree.
            p : First node.
            q : Second node.

        Returns:
            TreeNode of lowest common ancestor of p and q.

        """

        while True:
            if root.val < p.val and root.val < q.val:
                root = root.right
            elif root.val > p.val and root.val > q.val:
                root = root.left
            else:
                return root
