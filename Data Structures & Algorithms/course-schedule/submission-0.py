class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        dep_graph = defaultdict(list)
        dependent = set()

        for u, v in prerequisites:
            dep_graph[u].append(v)
            dependent.add(v)

        dfs = []

        for i in range(numCourses):
            if i not in dependent:
                dfs.append((i, set()))
        
        while dfs:
            curr_node, visited = dfs.pop()

            visited.add(curr_node)

            if len(visited) == numCourses:
                return True
            
            for i in dep_graph[curr_node]:
                if i not in visited:
                    dfs.append((i, visited.copy()))
            
        return False