class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        if len(tops) != len(bottoms):
            return -1
        
        hashMap = {}
        candidate = 0
        aRotations = 0
        bRotations = 0
        
        for i in range(0,len(tops)):
            if tops[i] in hashMap:
                hashMap[tops[i]] = hashMap[tops[i]] + 1
            else:
                hashMap[tops[i]] = 1
            
            if hashMap[tops[i]] >= len(tops): #can be tops or bottoms
                candidate = tops[i]
                break
            
            if bottoms[i] in hashMap:
                hashMap[bottoms[i]] = hashMap[bottoms[i]] + 1
            else:
                hashMap[bottoms[i]] = 1
                
            if hashMap[bottoms[i]] >= len(tops): #can be tops or bottoms
                candidate = bottoms[i]
                break
        
        #print(candidate)
        
        for i in range(0,len(tops)):
            if tops[i] != candidate and bottoms[i] != candidate:
                return -1
            elif tops[i] != candidate:
                aRotations += 1
            elif bottoms[i] != candidate:
                bRotations +=1
        
        return min(aRotations,bRotations)