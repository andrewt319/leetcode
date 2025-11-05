class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sol = nums[0]
        currSum = 0

        for num in nums:
            currSum = max(currSum + num, num)
            sol = max(currSum, sol)
        return sol
