实现 Trie (前缀树)
class Node:
    def __init__(self):
        self.s = [0 for i in range(26)]
        self.q = set()
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        
        now = self.root
        now.q.add(word)
        for i in word:
            if now.s[ord(i) - ord('a')] == 0:
                now.s[ord(i) - ord('a')] = Node()
            now = now.s[ord(i) - ord('a')]
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        now = self.root
        if word in now.q:
            return True
        return False
            
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        # root = Trie()
        now = self.root
        for i in prefix:
            if now.s[ord(i) - ord('a')] == 0:
                return False
            else:
                now = now.s[ord(i) - ord('a')]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
