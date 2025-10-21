class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int) -> int:
        sol = 0
        maxFreq = 1
        nums.sort()

        # Case 1: Using existing elements, and numOperations elements elements to equal those existing elements
        for i in range(len(nums)):
            # Get number with maxFrequency
            if i > 0 and nums[i] == nums[i - 1]:
                maxFreq += 1
            else:
                maxFreq = 1

            # Binary search to get numbers within [nums[i] - k, nums[i] + k]
            lowerBound, uppderBound = nums[i] - k, nums[i] + k
            leftIdx = bisect.bisect_left(nums, lowerBound)
            rightIdx = bisect.bisect_right(nums, uppderBound)

            # We can get rightIdx - leftIdx numbers the same, but can only do it to at most numOperations.
            # We can either change numOperations numbers to the number with max frequency, but only at most rightIdx - leftIdx. 
            maxNumbersEqual = min(maxFreq + numOperations, rightIdx - leftIdx)
            sol = max(maxNumbersEqual, sol)
        
        # Case 2: Creating numbers equal to a value that doesn't already exist in the array. 
        leftIdx = 0
        for i in range(len(nums)):
            # Find the range in the array where the number of numbers between [nums[left] , nums[left] + 2k] is maximized
            while nums[leftIdx] + (2 * k) < nums[i]:
                leftIdx += 1
            sol = max(sol, min(numOperations, i - leftIdx + 1))
        
        return sol
