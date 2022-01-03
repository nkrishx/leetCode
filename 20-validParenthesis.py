class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        
        for i in range(0,len(s)):
            if s[i]=='{':
                stack.append('}')
            elif s[i]=='(':
                stack.append(')')
            elif s[i]=='[':
                stack.append(']')
            elif len(stack)==0 or stack.pop()!=s[i]:
                return False
        if len(stack)!=0:
            return False
        return True
        