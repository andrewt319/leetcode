class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setNums = set(nums)
        sol = 0

        for num in setNums:
            if num - 1 in setNums:
                continue

            lengthSequence = 0
            currNum = num
            while currNum in setNums:
                lengthSequence += 1
                currNum += 1
            sol = max(sol, lengthSequence)
        
        return sol

