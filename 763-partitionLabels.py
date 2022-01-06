class Solution:
    '''
    we create a hashMap of all characters in the string with the last index(point)
    where they occur in the overall string, so we know that if we break the string at
    that point then there will be no occurance of the particular chjaracter in other partitions.
    We iterate through all of the characters one by one and go upto the point which is the
    last index of a character and is the highest among all characters seen till now.
    '''
    def partitionLabels(self, s: str) -> List[int]:
        hashMap={}
        
        for i in range(0,len(s)):
            hashMap[s[i]]=i
        
        start=0
        end=0
        result=[]
        
        for i in range(0,len(s)):
            end=max(end,hashMap[s[i]])
            if i==end:
                result.append(end-start+1)
                start=i+1
        
        return result
                
            