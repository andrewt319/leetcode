import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        sol = 0
        pq = []
        adjList = defaultdict(list)
        visited = [False for _ in range(n + 1)]
        visited[k] = True

        for source, target, weight in times:
            adjList[source].append((target, weight))
        
        for target, weight in adjList[k]:
            if not visited[target]:
                heapq.heappush(pq, (weight, target))
        
        while pq:
            currTime, currNode = heapq.heappop(pq)
            if visited[currNode]:
                continue
            
            sol = max(sol, currTime)
            visited[currNode] = True
            for target, weight in adjList[currNode]:
                if not visited[target]:
                    heapq.heappush(pq, (currTime + weight, target))
        
        return sol if sum(visited) == n else -1




