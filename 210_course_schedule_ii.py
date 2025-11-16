from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        sol = []
        courseToPre = defaultdict(list)

        # 1 = currently visiting, 0 not visited, 2 = visited
        visited = [0 for _ in range(numCourses)]

        for a, b in prerequisites:
            courseToPre[a].append(b)
        
        def dfs(course):
            if visited[course] == 1:
                return False
            elif visited[course] == 2:
                return True
            
            visited[course] = 1
            for pre in courseToPre[course]:
                if not dfs(pre):
                    return False
            visited[course] = 2
            sol.append(course)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []
        return sol
