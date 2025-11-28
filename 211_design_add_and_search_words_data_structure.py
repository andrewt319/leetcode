class Node:
    def __init__(self, isWord=False):
        self.isWord = isWord
        self.children = {}

class WordDictionary:

    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c in curr.children:
                curr = curr.children[c]
            else:
                curr.children[c] = Node()
                curr = curr.children[c]
        curr.isWord = True
        return

    def search(self, word: str) -> bool:
        return self.dfs(0, word, self.root)
    
    def dfs(self, idx: int, word: str, node: Node) -> bool:
        if idx == len(word):
            return node.isWord
        
        c = word[idx]
        if c != '.':
            if c not in node.children:
                return False
            return self.dfs(idx + 1, word, node.children[c])
            
        for nxt in node.children.values():
            if self.dfs(idx + 1, word, nxt):
                return True
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
