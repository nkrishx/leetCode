class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if len(tasks)==0:
            return 0
        
        maxFreq=0
        maxCount=0
        hashMap={}
        
        for i in range(0,len(tasks)):
            if tasks[i] not in hashMap:
                hashMap[tasks[i]]=0
            count=hashMap[tasks[i]]
            count+=1
            hashMap[tasks[i]]=count
            maxFreq=max(maxFreq,count)
        
        for key,val in hashMap.items():
            if val==maxFreq:
                maxCount+=1
        
        print(maxCount)
        print(maxFreq)
        
        partitions=maxFreq-1
        empty=partitions*(n-(maxCount-1))
        available=len(tasks)-maxFreq*maxCount
        idle=max(0,empty-available)
        return len(tasks)+idle
        