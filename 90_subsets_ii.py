class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        sol = []
        nums.sort()

        def bt(idx, curr):
            if idx > len(nums):
                return
                
            sol.append(curr.copy())
            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i - 1]:
                    continue
                curr.append(nums[i])
                bt(i + 1, curr)
                curr.pop()
        
        bt(0, [])
        return sol
