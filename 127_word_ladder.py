from collections import defaultdict, deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        wordSet = set(wordList)
        q = deque()
        q.append(beginWord)
        sol = 1
        while q:    
            for _ in range(len(q)):
                curr = q.popleft()
                if curr == endWord:
                    return sol

                for i, c in enumerate(curr):
                    for j in range(26):
                        newChar = chr(ord('a') + j)
                        if curr[i] == chr(ord('a') + j):
                            continue
                        currStr = curr[:i] + newChar + curr[i + 1:]
                        if currStr in wordSet:
                            q.append(currStr)
                            wordSet.remove(currStr)
            sol += 1 
        return 0
