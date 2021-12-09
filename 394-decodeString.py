class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        '''
        dfs pattern problem
        since we have nested operations here of brackets within brackets
        we decode the inner first and then move outwards
        we perform stack operations when we encounter '[' and ']'
        '''
        if(len(s) ==0):
            return ""
        numStack = []
        strStack = []
        num = 0
        currString = ""
        
        for i in range(0,len(s)):
            if s[i].isdigit(): #if digit we calculate the digit value of it from the string
                num = num * 10 + int(s[i])
            elif s[i] == '[':
                numStack.append(num)
                strStack.append(currString)
                print numStack
                print strStack
                num = 0
                currString = ""
            elif s[i] == ']':
                times = numStack.pop()
                newString = ""
                for each in range(0,times):
                    newString = newString+currString
                currString = strStack.pop()+newString
            else:
                currString = currString+s[i]
        
        return currString
        
        