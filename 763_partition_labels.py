class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        charToLatestIdx = [0] * 26
        for i, c in enumerate(s):
            charToLatestIdx[ord(c) - ord('a')] = i
        
        farthestIdx = leftIdx = 0
        sol = []
        for i, c in enumerate(s):
            farthestIdx = max(farthestIdx, charToLatestIdx[ord(c) - ord('a')])
            if i == farthestIdx:
                sol.append(i - leftIdx + 1)
                leftIdx = i + 1
        
        return sol
