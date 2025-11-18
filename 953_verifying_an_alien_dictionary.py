class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        charToIdx = {c:i for i,c in enumerate(order)}

        for i in range(1, len(words)):
            word1, word2 = words[i - 1], words[i]

            for j in range(min(len(word1), len(word2))):
                if charToIdx[word1[j]] > charToIdx[word2[j]]:
                    return False
                elif charToIdx[word1[j]] < charToIdx[word2[j]]:
                    break
            else:
                if len(word1) > len(word2):
                    return False
        
        return True

