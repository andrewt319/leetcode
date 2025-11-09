class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s))]

        for i in range(len(s)):
            for word in wordDict:
                startIdx = i - len(word) + 1
                if s[startIdx:i + 1] == word and (dp[startIdx - 1] == True or startIdx - 1 < 0):
                    dp[i] = True
                    break
        return dp[-1]        
            
