from collections import Counter
class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        sol = 0

        for item, count in Counter(tasks).items():
            if count == 1:
                return -1

            sol += count // 3
            if count % 3 != 0:
                sol += 1
        return sol
            
