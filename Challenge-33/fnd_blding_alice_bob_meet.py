import heapq


class Solution:
    def leftmostBuildingQueries(self, heights: list[int], queries: list[list[int]]) -> list[int]:
        '''
        Find Building Where Alice and Bob Can Meet
        
        Args:
            heights:array of heights , where heights[i] represents the height of the ith building.
            queries:array of queries where queries[i] = [ai, bi]. On the ith query, Alice is in 
                    building ai while Bob is in building bi.
        Return:
             array of ans where ans[i] is the index of the leftmost building where 
             Alice and Bob can meet on the ith query.
        '''
        res=[-1]*len(queries)
        groups={}

        for i, q in enumerate(queries):
            l,r = sorted(q)
            if l ==r or heights[l]<heights[r]:
                res[i] = r
            else:
                h=max(heights[l],heights[r])
                if r not in groups:
                    groups[r]=[(h,i)]
                else:
                    groups[r].append((h,i))
        
        min_heap=[]
        for i, h in enumerate(heights):
            for q_h,q_i in groups.get(i,[]):
                heapq.heappush(min_heap,(q_h,q_i))
            
            while min_heap and h> min_heap[0][0]:
                q_h, q_i = heapq.heappop(min_heap)
                res[q_i] = i
        
        return res

            
            