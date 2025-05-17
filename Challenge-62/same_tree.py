# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        Determines if two binary trees are structurally identical and have the same node values.
        Args:
            p, q: The root nodes of input binary trees
        Returns:
            True if the two binary trees are the same, False otherwise.
        '''
        
        def dfs(node1, node2):
            if not node1 and not node2:
                return True
            
            if (node1 and not node2) or (node2 and not node1 )or node1.val != node2.val:
                return False

            left = dfs(node1.left, node2.left)
            right = dfs(node1.right, node2.right)

            return left and right
        return dfs(p,q)
            

            
            