
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    '''
    Create a deep copy (clone) of graph
    Args:
        node:Reference of a node in a connected undirected graph.
    Returns:
        Return a deep copy (clone) of the graph.
    '''
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new={}

        def dfs(node):
            if not node:
                return
            if node in old_to_new:
                return old_to_new[node]
            copy=Node(node.val)
            old_to_new[node]=copy
            for nei in node.neighbors:
                copy_nei=dfs(nei)
                copy.neighbors.append(copy_nei)
            return copy
        
        return dfs(node)
        