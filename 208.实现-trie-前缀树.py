#
# @lc app=leetcode.cn id=208 lang=python
#
# [208] 实现 Trie (前缀树)
#

# @lc code=start
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.children = [None for _ in range(26)]
        self.is_end = False

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        node = self
        for ch in word:
            index = ord(ch) - ord('a')
            if node.children[index] is None:
                node.children[index] = Trie()
            node = node.children[index]
        node.is_end = True            

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self
        for ch in word:
            index = ord(ch) - ord('a')
            if node.children[index] is None:
                return False
            node = node.children[index]
        return node.is_end == True   

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self
        for ch in prefix:
            index = ord(ch) - ord('a')
            if node.children[index] is None:
                return False
            node = node.children[index]
        return True   




# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# @lc code=end

