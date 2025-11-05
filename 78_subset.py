class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol = []

        def bt(idx, curr):
            if idx > len(nums):
                return
            elif idx == len(nums):
                sol.append(curr.copy())
                return

            curr.append(nums[idx])
            bt(idx + 1, curr)
            curr.pop()
            bt(idx + 1, curr)
        
        bt(0, [])
        return sol
