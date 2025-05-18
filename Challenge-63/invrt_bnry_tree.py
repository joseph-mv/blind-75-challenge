from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Inverts a binary tree using BFS .

        Args:
            root : The root node of the binary tree.

        Returns:
            The root node of the inverted binary tree.
        """

        q = [root]
        while q:
            curr = q.pop(0)
            if not curr:
                continue

            curr.left, curr.right = curr.right, curr.left

            q.append(curr.left)
            q.append(curr.right)

        return root
