from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> list[list[int]]:
        """
        Performs level order traversal of a binary tree.
        Traverses the tree level by level from left to right and collects values of nodes at each level.

        Args:
            root : The root node of the binary tree.

        Returns:
            A list where each sublist contains the node values at each level of the tree.

        """
        if not root:
            return []
        res = []
        q = [root]

        while q:
            lev = []
            for i in range(len(q)):
                curr = q.pop(0)
                lev.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)

            res.append(lev)
        return res
