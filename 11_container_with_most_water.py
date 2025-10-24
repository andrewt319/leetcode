class Solution:
    def maxArea(self, height: List[int]) -> int:
        sol = 0
        l, r = 0, len(height) - 1

        while l < r:
            if height[l] < height[r]:
                sol = max(sol, height[l] * (r - l))
                l += 1
            else:
                sol = max(sol, height[r] * (r - l))
                r -= 1
                
        return sol
