class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[1], x[0]))
        sol = 0
        prevEnd = intervals[0][1]
        
        for i in range(1, len(intervals)):
            currStart, currEnd = intervals[i]
            if currStart < prevEnd:
                sol += 1
            else:
                prevEnd = currEnd
        
        return sol




