class Solution:
    '''
    use a stack to put elements which are unresolved 
    and then compare with incoming element if its greater than the 
    top element in the stack (resolves it), if so then calculate the
    value for it and push the incoming on to the stack
    '''
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        if len(T)==0:
            return []
        
        arr = [0 for i in range(0,len(T))]
        stack = []
        
        for idx, val in enumerate(T):
            while len(stack)!=0 and T[idx]>T[stack[-1]]:
                i = stack.pop()
                arr[i] = idx - i
            
            stack.append(idx)
    
        return arr
        