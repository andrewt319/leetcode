class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0

        currEnd = currFarthest = minJumps = 0
        for i in range(len(nums)):
            currFarthest = max(currFarthest, nums[i] + i)

            if currFarthest >= len(nums) - 1:
                return minJumps + 1
            
            if i == currEnd:
                currEnd = currFarthest
                minJumps += 1
