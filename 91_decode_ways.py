class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        
        dp = [0] * len(s)
        dp[0] = 1
        for i in range(1, len(s)):
            curr = 0

            if s[i] != "0":
                curr += dp[i - 1]
            if 10 <= int(s[i - 1] + s[i]) <= 26:
                curr += dp[i - 2] if i >= 2 else 1
            dp[i] = curr
        
        return dp[-1] 

