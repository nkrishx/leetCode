class TrieNode:
    def __init__(self):
        self.word = ""
        self.children = [None for each in range(0,26)]
    
class Solution(object):
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self,word):
        """
        :type word: str
        :rtype: None
        """
        '''
        we set here the given word value as word for the 
        last character of the word, meaning its the end and also is the word in 
        dictionary
        '''
        curr = self.root
        for c in word:
            ord_val = ord(c)-ord('a')
            if curr.children[ord_val] is None:
                curr.children[ord_val] = TrieNode()
            curr = curr.children[ord_val]
        curr.word = word
        
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        '''
        tries with bfs solution, 
        bfs since we are building successive words and we will shunt out any 
        children of an element which is not in the dictionary word list
        we will also change the boolean value inside the TrieNode class object 
        since we also want the actual word along with if its the end of a word
        '''
        for word in words:
            self.insert(word)
        
        
        curr = self.root
        queue = collections.deque()
        queue.append(curr)
        while(len(queue)!=0):
            curr = queue.popleft()
            for each in range (25,-1,-1):
                if curr.children[each] and curr.children[each].word:
                    queue.append(curr.children[each])
        return curr.word
        