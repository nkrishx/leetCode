class Solution:
    '''
    end is the represented as a block number,
    i,e. for a process 2 if start is 3 and end is 3, it means 
    a value of 1, hence we need to add a +1 to the current process time to get the correct value
    '''
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        result = [0 for i in range(0,n)]
        
        if len(logs)==0:
            return result
        
        previous=0
        stack=[]
        
        for i in range(0,len(logs)):
            s=logs[i].split(":") #[0,start,0]
            current=int(s[2])
            if s[1]=="start":
                if len(stack)!=0:
                    result[stack[-1]]+=current-previous
                    previous=current
                stack.append(int(s[0]))
            else:
                result[stack.pop()]+=current+1-previous
                previous=current+1
        
        return result
                