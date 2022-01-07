class Solution:
    '''
    bfs would a better solution when compared with dfs
    since we don't want to explore all babies once we have a valid case.
    On average bfs is better when compared with dfs and dfs solution might
    require deepcopy and bscktracking
    '''
    def removeInvalidParentheses(self, s: str) -> List[str]:
        queue=collections.deque()
        hashSet=set()
        
        queue.append(s)
        hashSet.add(s)
        result=[]
        flag=False
        
        while(len(queue)!=0 and flag==False):
            size=len(queue)
            
            for i in range(0,size):
                curr=queue.popleft()
                if self.isValid(curr):
                    result.append(curr)
                    flag=True
                if flag!=True:
                    for j in range(0,len(curr)):
                        curr_str=curr[0:j]+curr[j+1:]
                        if curr_str not in hashSet:
                            queue.append(curr_str)
                            hashSet.add(curr_str)
        
        return result
    
    def isValid(self,s):
        count=0
        for i in range(0,len(s)):
            if s[i]=='(':
                count+=1
            elif s[i]==')':
                if count==0:
                    return False
                count-=1
        if count==0:
            return True