class Solution:
    def checkValidString(self, s: str) -> bool:
        minNumOpen = maxNumOpen = 0

        for c in s:
            if c == '(':
                minNumOpen += 1
                maxNumOpen += 1
            elif c == ')':
                minNumOpen -= 1
                maxNumOpen -= 1
            elif c == '*':
                minNumOpen -= 1
                maxNumOpen += 1

            if maxNumOpen < 0:
                return False
            minNumOpen = max(minNumOpen, 0)        
        return minNumOpen == 0
