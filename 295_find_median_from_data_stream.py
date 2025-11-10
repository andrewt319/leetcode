import heapq
class MedianFinder:

    def __init__(self):
        self.lower = []
        self.upper = []

    def addNum(self, num: int) -> None:
        if len(self.lower) > len(self.upper):
            heapq.heappush(self.lower, -num)
            middle = -heapq.heappop(self.lower)
            heapq.heappush(self.upper, middle)
        elif len(self.upper) >= len(self.lower):
            heapq.heappush(self.upper, num)
            middle = -heapq.heappop(self.upper)
            heapq.heappush(self.lower, middle)

    def findMedian(self) -> float:
        if len(self.lower) > len(self.upper):
            return -self.lower[0]
        elif len(self.upper) > len(self.lower):
            return self.upper[0]
        else:
            return (-self.lower[0] + self.upper[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
