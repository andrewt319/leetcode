class Solution:
    def countSubstrings(self, s: str) -> int:
        sol = 0
        n = len(s)

        for i in range(n):
            l = r = i
            while l >= 0 and r < n and s[l] == s[r]:
                sol += 1
                l -=1
                r += 1
            
            l = i
            r = i + 1
            while l >= 0 and r < n and s[l] == s[r]:
                sol += 1
                l -= 1
                r += 1
        return sol
