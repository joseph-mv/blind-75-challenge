# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        """
        Binary Tree Maximum Path Sum
            A path in a binary tree is a sequence of nodes where each pair of adjacent nodes
            in the sequence has an edge connecting them. A node can only appear in the sequence
            at most once. Note that the path does not need to pass through the root.

            The path sum of a path is the sum of the node's values in the path.

        Args:
            root : The root node of the binary tree.

        Returns:
            The maximum path sum of any non-empty path in the tree.

        """
        res = root.val

        def dfs(root):
            nonlocal res
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            left = max(left, 0)
            right = max(right, 0)

            res = max(res, root.val + left + right)
            return root.val + max(left, right)

        dfs(root)
        return res
