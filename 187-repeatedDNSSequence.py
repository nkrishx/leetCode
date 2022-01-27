class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        result = set()
        sequences = set()
        
        if len(s) < 10:
            return []
        
        for i in range(0,len(s)+1-10):
            if s[i:i+10] in sequences:
                result.add(s[i:i+10])
            sequences.add(s[i:i+10])
    
        return result