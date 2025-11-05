class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        sol = []

        def bt(idx, currArr, currSum):
            if idx >= len(candidates) or currSum > target:
                return
            elif currSum == target:
                sol.append(currArr.copy())
                return
            
            for i in range(idx, len(candidates)):
                currArr.append(candidates[i])
                bt(i, currArr, currSum + candidates[i])
                currArr.pop()
        
        bt(0, [], 0)
        return sol
