import bisect
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = [nums[0]]

        for i in range(1, len(nums)):
            idx = bisect.bisect_left(tails, nums[i])
            if idx >= len(tails):
                tails.append(nums[i])
            else:
                tails[idx] = nums[i]
        return len(tails)
            

        # dp = [1] * len(nums)

        # for i in range(1, len(nums)):
        #     for j in range(i):
        #         if nums[i] > nums[j]:
        #             dp[i] = max(dp[i], dp[j] + 1)

        # return max(dp)
