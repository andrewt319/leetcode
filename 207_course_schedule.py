from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(course):
            if visitedStatus[course] == 2:
                return True
            elif visitedStatus[course] == 1:
                return False
            
            visitedStatus[course] = 1
            for preReq in courseToPrereq[course]:
                if not dfs(preReq):
                    return False
            visitedStatus[course] = 2
            return True

        # 1 is currentlyVisiting, 2 is visited
        visitedStatus = defaultdict(int)
        courseToPrereq = defaultdict(list)
        for course, preReq in prerequisites:
            courseToPrereq[course].append(preReq)

        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
