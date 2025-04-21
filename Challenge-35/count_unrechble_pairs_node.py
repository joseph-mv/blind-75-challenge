from collections import defaultdict

class Solution:
    def countPairs(self, n: int, edges: list[list[int]]) -> int:
        """
        Count the number of pairs of nodes that are unreachable from each other in an undirected graph.

        Args:
            n: Number of nodes in the graph, labeled from 0 to n-1.
            edges: List of undirected edges where each edge connects two nodes.

        Returns:
            Total number of pairs of different nodes that are unreachable from each other.
        """
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visited = [False] * n

        def dfs(node):
            stack = [node]
            size = 0
            while stack:
                curr = stack.pop()
                if not visited[curr]:
                    visited[curr] = True
                    size += 1
                    for neighbor in graph[curr]:
                        if not visited[neighbor]:
                            stack.append(neighbor)
            return size

        total_pairs = n * (n - 1) // 2 
        reachable_pairs = 0

        for i in range(n):
            if not visited[i]:
                component_size = dfs(i)              
                reachable_pairs += component_size * (component_size - 1) // 2

        return total_pairs - reachable_pairs