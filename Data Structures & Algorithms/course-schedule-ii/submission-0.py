class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        indegree = [0] * numCourses
        adj = [[] for i in range(numCourses)]

        for u,v in prerequisites:
            indegree[v] +=1
            adj[u].append(v)

        q = deque()

        for n in range(numCourses):
            if indegree[n] == 0:
                q.append(n)

        finish, output = 0,[]

        while q :
            node = q.popleft()

            output.append(node)
            finish +=1

            for nei in adj[node]:
                indegree[nei]-=1

                if indegree[nei] == 0:
                    q.append(nei)

        
        if finish != numCourses:
            return []

        return output[::-1]