class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        prevUnique = float('-inf')
        count = 0

        for num in nums:
            candidate = max(num - k, prevUnique + 1)
            if candidate <= num + k:
                count += 1
                prevUnique = candidate
        
        return count
