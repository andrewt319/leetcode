class MinStack:

    def __init__(self):
        self.minArr = []
        self.arr = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        self.minArr.append(val if len(self.minArr) == 0 else min(val, self.minArr[-1]))

    def pop(self) -> None:
        self.arr.pop()
        self.minArr.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.minArr[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
