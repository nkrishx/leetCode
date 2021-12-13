class TrieNode:
    def __init__(self):
        '''
        isEnd is to indicate if the end of a word that was inserted
        26 characters since all lower case chars, if special chars then we can use more
        '''
        self.isEnd = False
        self.children = [None for each in range(0,26)]
        

class Solution(object):
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
    
    def replaceWords(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        for word in dictionary:
            self.insert(word)
            
        result = []
        split_sentence = sentence.split(" ")
        
        for word in split_sentence:
            curr = self.root
            s = []
            for c in word:
                ord_val = ord(c)-ord('a')
                #we break out in 2 cases when we find the that we have traversed
                #to an isEnd true, meaning we have a short hand for the word or if
                #we have a different charcter in between
                if curr.children[ord_val] is None or curr.isEnd == True:
                    break
                s.append(c)
                curr = curr.children[ord_val]
            if curr.isEnd == True:
                result.append("".join(s))
            else:
                result.append(word)
                
        return " ".join(result)
            
                    
                
        
        
        
        