class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIdx = {c: i for i, c in enumerate(s)}
        furthest = left = 0
        sol = []

        for i in range(len(s)):
            furthest = max(furthest, lastIdx[s[i]])

            if i == furthest:
                sol.append(furthest - left + 1)
                left = furthest + 1

        return sol
