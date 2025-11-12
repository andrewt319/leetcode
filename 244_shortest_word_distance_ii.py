from collections import defaultdict
class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.invertedIdx = defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.invertedIdx[word].append(i)
        
    def shortest(self, word1: str, word2: str) -> int:
        word1Idx = word2Idx = 0
        sol = float('inf')

        while word1Idx < len(self.invertedIdx[word1]) and word2Idx < len(self.invertedIdx[word2]):
            sol = min(sol, abs(self.invertedIdx[word1][word1Idx] - self.invertedIdx[word2][word2Idx]))

            if self.invertedIdx[word1][word1Idx] < self.invertedIdx[word2][word2Idx]:
                word1Idx += 1
            else:
                word2Idx += 1
        
        return sol


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)
