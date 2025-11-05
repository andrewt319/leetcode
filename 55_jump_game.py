class Solution:
    def canJump(self, nums: List[int]) -> bool:
        earliestIdx = len(nums) - 1

        for i in range(len(nums) -1, -1, -1):
            if i + nums[i] >= earliestIdx:
                earliestIdx = i
        
        return earliestIdx == 0 
