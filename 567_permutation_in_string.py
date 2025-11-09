from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1CharCount = defaultdict(int)
        s2CharCount = defaultdict(int)
        for i in range(len(s1)):
            s1CharCount[s1[i]] += 1
            s2CharCount[s2[i]] += 1
        
        l = 0
        for r in range(len(s1), len(s2)):
            if s1CharCount == s2CharCount:
                return True
            s2CharCount[s2[l]] -= 1
            s2CharCount[s2[r]] += 1

            if s2CharCount[s2[l]] == 0:
                s2CharCount.pop(s2[l])
            l += 1

        return s1CharCount == s2CharCount

