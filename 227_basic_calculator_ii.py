class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        sign = '+'
        currNum = 0

        def updateStack(currNum, sign):
            if sign == '+':
                stack.append(currNum)
            elif sign == '-':
                stack.append(-currNum)
            elif sign == '/':
                stack[-1] = int(stack[-1] / currNum)
            elif sign == '*':
                stack[-1] *= currNum

        for c in s:
            if c.isdigit():
                currNum = currNum * 10 + int(c)
            elif c in "+-/*":
                updateStack(currNum, sign)
                currNum = 0
                sign = c
        
        updateStack(currNum, sign)
        return sum(stack)
