class Solution:
    '''
    slidign window solution with hashMap
    we setup a hashmap with all elements of the compare string (p)
    we increment and decrements counts and complete match of the string and determine the index
    '''
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hashMap = {}
        
        for i in p:
            if i not in hashMap:
                hashMap[i] = 0
            hashMap[i] = hashMap[i]+1
            
        match = 0
        result=[]
        
        # print(hashMap)
        
        for i in range(0,len(s)):
            if s[i] in hashMap:
                count = hashMap[s[i]]
                count-=1
                hashMap[s[i]]=count
                if count==0:
                    match+=1
            if i>=len(p):
                if s[i-len(p)] in hashMap:
                    c=hashMap[s[i-len(p)]]
                    c+=1
                    hashMap[s[i-len(p)]] = c
                    if c==1:
                        match-=1
            if match==len(hashMap):
                result.append(i-len(p)+1)
                
        return result
                    
                