class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [0 for _ in range(len(nums))]
        currProd = 1
        for i in range(len(nums)):
            left[i] = currProd
            currProd *= nums[i]
        
        right = [0 for _ in range(len(nums))]
        currProd = 1
        for i in range(len(nums) - 1, -1, -1):
            right[i] = currProd
            currProd *= nums[i]
        
        sol = []
        for l, r in zip(left, right):
            sol.append(l * r)
        return sol
