class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == '/':
                top = stack.pop()
                stack[-1] = int(stack[-1] / top)
            elif token == '+':
                top = stack.pop()
                stack[-1] += top
            elif token == '-':
                top = stack.pop()
                stack[-1] -= top
            elif token == '*':
                top = stack.pop()
                stack[-1] *= top
            else:
                stack.append(int(token))

        return sum(stack)
