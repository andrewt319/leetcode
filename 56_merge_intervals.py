class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        stack = [intervals[0]]

        for i in range(1, len(intervals)):
            prevX, prevY = stack[-1]
            currX, currY = intervals[i]

            if currX <= prevY:
                stack[-1][1] = max(prevY, currY)
            else:
                stack.append([currX, currY])
        return stack
