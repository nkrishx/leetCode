class Solution:
    '''
    for a solution to exist we need an element whose count is equal or
    greater than the size of the arrays
    commented hashMap solution
    
    we can have an optimized solution without the hashMap
    if we have a viable solution then it should be an element in an index i pair
    meanining a vaible solution can be a[0] or b[0] for the index pair 0,
    we can choose any i value for this
    '''
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        if len(tops) != len(bottoms):
            return -1
        
        result = self.check(tops,bottoms,tops[0])
        
        if result != -1:
            return result
        
        return self.check(tops,bottoms,bottoms[0])
        
    def check(self,tops,bottoms,target):
        topsRotations = 0
        bottomsRotations = 0
        for i in range(0,len(tops)): #can be tops or bottoms
            if tops[i] != target and bottoms[i] != target:
                return -1
            elif tops[i] != target:
                topsRotations += 1
            elif bottoms[i] != target:
                bottomsRotations +=1
        
        return min(topsRotations,bottomsRotations)


        
    # def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
    #     if len(tops) != len(bottoms):
    #         return -1
        
    #     hashMap = {}
    #     candidate = 0
    #     topsRotations = 0
    #     bottomsRotations = 0
        
    #     for i in range(0,len(tops)):
    #         if tops[i] in hashMap:
    #             hashMap[tops[i]] = hashMap[tops[i]] + 1
    #         else:
    #             hashMap[tops[i]] = 1
            
    #         if hashMap[tops[i]] >= len(tops): #can be tops or bottoms
    #             candidate = tops[i]
    #             break
            
    #         if bottoms[i] in hashMap:
    #             hashMap[bottoms[i]] = hashMap[bottoms[i]] + 1
    #         else:
    #             hashMap[bottoms[i]] = 1
                
    #         if hashMap[bottoms[i]] >= len(tops): #can be tops or bottoms
    #             candidate = bottoms[i]
    #             break
        
    #     #print(candidate)
        
    #     for i in range(0,len(tops)):
    #         if tops[i] != candidate and bottoms[i] != candidate:
    #             return -1
    #         elif tops[i] != candidate:
    #             topsRotations += 1
    #         elif bottoms[i] != candidate:
    #             bottomsRotations +=1
        
    #     return min(topsRotations,bottomsRotations)