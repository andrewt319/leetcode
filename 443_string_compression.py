class Solution:
    def compress(self, chars: List[str]) -> int:
        l = 0
        currCount = 1

        for i in range(1, len(chars) + 1):
            if i < len(chars) and chars[i] == chars[i - 1]:
                currCount += 1
            else:
                chars[l] = chars[i - 1]
                l += 1
                
                if currCount > 1:
                    for c in str(currCount):
                        chars[l] = c
                        l += 1
                
                if i < len(chars):
                    currCount = 1
        
        return l
