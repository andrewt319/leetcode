class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        target = sum(nums)
        if target % 2 != 0:
            return False
        target //= 2

        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for i in range(target, -1, -1):
                dp[i] = dp[i] or (dp[i - num] if i - num >= 0 else False)

        return dp[-1]
