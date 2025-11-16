class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # kruskals
        n = len(points)
        edges = []

        for i in range(n - 1):
            a, b = points[i]
            for j in range(i + 1, n):
                c, d = points[j]
                edges.append((abs(a - c) + abs(b - d), i, j))
        
        parents = [i for i in range(n)]
        size = [1] * n
        def union(a, b):
            parentA, parentB = find(a), find(b)

            if parentA == parentB:
                return False 
            
            if size[parentA] < size[parentB]:
                parentA, parentB = parentB, parentA
            
            parents[parentB] = parentA
            size[parentA] += size[parentB]
            return True
        
        def find(a):
            while parents[a] != a:
                parents[a] = parents[parents[a]]
                a = parents[a]
            return a
        
        edges.sort()
        numEdges = 0
        sol = 0
        for cost, i, j in edges:
            if not union(i, j):
                continue
            elif numEdges == len(points) - 1:
                break
            numEdges += 1
            sol += cost
        return sol
