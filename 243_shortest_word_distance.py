class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        word1Idx = word2Idx = -1
        sol = float('inf')

        for i, word in enumerate(wordsDict):
            if word == word1:
                word1Idx = i
            elif word == word2:
                word2Idx = i

            if word1Idx != -1 and word2Idx != -1:
                sol = min(abs(word1Idx - word2Idx), sol)
        
        return sol
