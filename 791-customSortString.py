class Solution:
    '''
    hashMap solution, add all elements into the map and their occurances
    then build the output string as per the order given and then append all
    the remaining characters
    '''
    def customSortString(self, order: str, s: str) -> str:
        if len(s)==0 or s is None:
            return s
        
        if len(order)==0 or order is None:
            return s
        
        hashMap={}
        result=""
        
        for each in s:
            if each not in hashMap:
                hashMap[each] = 0
            hashMap[each]+=1
            
        for c in order:
            if c in hashMap:
                count = hashMap[c]
                while(count!=0):
                    result=result+c
                    count-=1
                del hashMap[c]
        
        for key,val in hashMap.items():
            count=hashMap[key]
            while(count!=0):
                result=result+key
                count-=1
        
        return result
        