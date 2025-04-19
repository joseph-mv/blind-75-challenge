from collections import defaultdict


class Solution:
    def maxStarSum(self, vals: list[int], edges: list[list[int]], k: int) -> int:
        """
        Calculates the maximum star sum in an undirected graph.
        
        A star graph is a subgraph of the given graph having a center node containing 0 or more neighbors. 
        In other words, it is a subset of edges of the given graph such that there exists a common node for all edges.
        
        Args:
            vals : array of values of each node.
            edges :array of  undirected edges between nodes.
            k : Maximum number of neighbors in the star graph.

        Returns:
             The maximum star sum .
        """
        max_star_sum=max(vals)
        graph=defaultdict(list)

        for i, j in edges:
            graph[i].append(vals[j])
            graph[j].append(vals[i])
        
        for key, values in graph.items():
            values.sort(reverse=True)
            star_sum=vals[key]
            i=0
            while i<k and i<len(values) and values[i]>=0: 
                star_sum+=values[i]
                i+=1
            max_star_sum=max(max_star_sum,star_sum)
        return max_star_sum
        