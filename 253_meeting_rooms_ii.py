import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ends = [intervals[0][1]]
        sol = numRooms = 1

        for i in range(1, len(intervals)):
            currStart, currEnd = intervals[i]

            earliestEnd = ends[0]
            if currStart < earliestEnd:
                numRooms += 1
            else:
                heapq.heappop(ends)
            heapq.heappush(ends, currEnd)
            sol = max(sol, numRooms)
        return sol
