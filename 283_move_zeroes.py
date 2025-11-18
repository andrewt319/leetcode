class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0

        for i in range(len(nums)):
            if nums[slow] != 0:
                slow += 1
            elif nums[slow] == 0 and nums[i] != 0:
                nums[slow], nums[i] = nums[i], nums[slow]
                slow += 1
