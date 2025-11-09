class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        sol = []

        def bt(curr, currSet):
            if len(curr) == len(nums):
                sol.append(curr.copy())
                return
            elif len(curr) > len(nums):
                return
            
            for num in nums:
                if num in currSet:
                    continue
                curr.append(num)
                currSet.add(num)
                bt(curr, currSet)
                curr.pop()
                currSet.remove(num)
        
        bt([], set())
        return sol
