class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [i for i in range(len(edges) + 1)]
        sizes = [1] * (len(edges) + 1)

        def union(a, b):
            parentA, parentB = find(a), find(b)
            if parentA == parentB:
                return False
            
            if sizes[parentA] > sizes[parentB]:
                parents[parentB] = parentA
                sizes[parentA] += sizes[parentB]
            else:
                parents[parentA] = parentB
                sizes[parentB] += sizes[parentA]
            return True

        def find(a):
            while parents[a] != a:
                prev = a
                a = parents[a]
                parents[prev] = a
            return a
        
        for a, b in edges:
            if not union(a, b):
                return [a, b]
        
