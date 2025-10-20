class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        sol = [0 for _ in range(len(temperatures))]

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                idx, prevTemp = stack.pop()
                sol[idx] = i - idx
            stack.append((i, temp))
        
        return sol

