class TrieNode:
    def __init__(self):
        '''
        isEnd is to indicate if the end of a word that was inserted
        26 characters since all lower case chars, if special chars then we can use more
        '''
        self.isEnd = False
        self.children = [None for each in range(0,26)]
    
class Trie(object):

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        :type word: str
        :rtype: None
        """
        curr = self.root
        for c in word:
            ord_val = ord(c)-ord('a')
            if curr.children[ord_val] is None:
                curr.children[ord_val] = TrieNode()
            curr = curr.children[ord_val]
        curr.isEnd = True
        

    def search(self, word):
        """
        :type word: str
        :rtype: bool
        """
        curr = self.root
        for c in word:
            ord_val = ord(c)-ord('a')
            if curr.children[ord_val] is None:
                return False
            curr = curr.children[ord_val]
        return curr.isEnd
        
        
    def startsWith(self, prefix):
        """
        :type prefix: str
        :rtype: bool
        """
        curr = self.root
        for c in prefix:
            ord_val = ord(c)-ord('a')
            if curr.children[ord_val] is None:
                return False
            curr = curr.children[ord_val]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)