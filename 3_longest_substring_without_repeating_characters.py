class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sol = l = 0
        uniqueChars = set()

        for r in range(len(s)):
            while l < r and s[r] in uniqueChars:
                uniqueChars.remove(s[l])
                l += 1
            uniqueChars.add(s[r])
            sol = max(sol, len(uniqueChars))

        return sol
