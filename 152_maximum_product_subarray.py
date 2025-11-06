class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minProd = maxProd = 1
        sol = float('-inf')

        for num in nums:
            minProd, maxProd = min(minProd * num, maxProd * num, num), max(minProd * num, maxProd * num, num)
            sol = max(sol, minProd, maxProd)
        
        return sol
