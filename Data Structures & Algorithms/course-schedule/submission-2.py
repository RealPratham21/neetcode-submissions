class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        
        queue = []

        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        processed = 0

        while queue:
            cnode = queue.pop()
            processed += 1

            for i in graph[cnode]:
                indegree[i] -= 1
            
                if indegree[i] == 0:
                    queue.append(i)
        
        return processed == numCourses