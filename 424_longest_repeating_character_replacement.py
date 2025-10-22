from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        sol = l = 0
        charCount = defaultdict(int)
        maxFreq = 0

        for r in range(len(s)):
            charCount[s[r]] += 1
            maxFreq = max(maxFreq, charCount[s[r]])

            # Number of elements that aren't the character that shows up the most between [l, r]
            while l < r and r - l + 1 - maxFreq > k:
                charCount[s[l]] -= 1
                l += 1
            
            sol = max(sol, r - l + 1)
        
        return sol
