class Solution:

    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        """
        Determines if it is possible to finish all courses given their prerequisites.

        Args:
            numCourses (int): Total number of courses labeled from 0 to numCourses - 1.
            prerequisites (List[List[int]]): List of [a, b] pairs where course 'b' 
            must be completed before course 'a'.

        Returns:
             bool: True if it's possible to finish all courses (i.e., no cycles), False otherwise.
        """
        graph={}
        inDegree=[0]*numCourses

        for [a,b] in prerequisites:
            if not graph.get(b):
                graph[b]=[]
            graph[b].append(a)
            inDegree[a]+=1
        
        queue=[]
        for i in range(numCourses):
            if inDegree[i]==0:
                queue.append(i)
        
        completed=0
        while len(queue):
            course=queue.pop(0)
            completed+=1
            
            for nei in graph.get(course,[]):
                inDegree[nei]-=1
                if (inDegree[nei]==0):
                    queue.append(nei)

        return completed==numCourses
                
