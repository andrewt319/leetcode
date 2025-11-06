class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        sol = []
        candidates.sort()

        def bt(idx, currArr, currSum):
            if currSum == target:
                sol.append(currArr.copy())
                return
            elif currSum > target or idx >= len(candidates):
                return 
            
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                currArr.append(candidates[i])
                bt(i + 1, currArr, candidates[i] + currSum)
                currArr.pop()
        
        bt(0, [], 0)
        return sol
