class Solution:
    def calculate(self, s: str) -> int:
        def calc(idx):
            sign = 1
            currNum = 0
            stack = []

            while idx < len(s):
                c = s[idx]
                if c.isdigit():
                    currNum = currNum * 10 + int(c)
                elif c in "+-":
                    stack.append(sign * currNum)
                    sign = 1 if c == "+" else -1
                    currNum = 0
                elif c == "(":
                    currNum, idx = calc(idx + 1)
                elif c == ")":
                    stack.append(sign * currNum)
                    return sum(stack), idx
                idx += 1
            stack.append(sign * currNum)
            return sum(stack)
        
        return calc(0)



