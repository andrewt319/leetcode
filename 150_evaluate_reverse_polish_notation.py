class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for c in tokens:
            if c == '+':
                stack[-2] += stack[-1]
                stack.pop()
            elif c == '-':
                stack[-2] -= stack[-1]
                stack.pop()
            elif c == '/':
                stack[-2] = int(stack[-2] / stack[-1])
                stack.pop()
            elif c == '*':
                stack[-2] *= stack[-1]
                stack.pop()
            else:
                stack.append(int(c))
        
        return stack[0]
