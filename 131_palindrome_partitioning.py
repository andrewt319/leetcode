class Solution:
    def partition(self, s: str) -> List[List[str]]:
        sol = []

        def isPalindrome(word):
            l, r = 0, len(word) - 1
            while l < r:
                if word[l] != word[r]:
                    return False
                l += 1
                r -= 1
            return True

        def bt(s, curr):
            if s == '':
                sol.append(curr.copy())
                return
            
            for i in range(1, len(s) + 1):
                if isPalindrome(s[:i]):
                    curr.append(s[:i])
                    bt(s[i:], curr)
                    curr.pop()
        
        bt(s, [])
        return sol
