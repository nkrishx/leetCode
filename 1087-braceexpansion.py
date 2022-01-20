class Solution:
    def expand(self, S: str) -> List[str]:
        if len(S) == 0:
            return []
        size = len(S)
        i = 0
        self.result = []
        blocks=[]
        while i< size:
            block = []
            if S[i] == '{':
                i = i+1
                while S[i] != '}':
                    if S[i] != ',':
                        block.append(S[i])
                    i+=1
                blocks.append(block)
            else:        
                block.append(S[i])
                blocks.append(block)
            i +=1
        print(blocks)
        self.backtrack(blocks, 0, [])
        return sorted(self.result)
    
    def backtrack(self,words, idx, result):
        #Base
        if len(words) == idx:
            self.result.append(''.join(result))
            return
            
        #Logic
        
        for c in words[idx]:
            result.append(c)
            self.backtrack(words, idx+1, result)
            result.pop()
            
        return
        
        
        
    
            
            
            
            
            
                    
        