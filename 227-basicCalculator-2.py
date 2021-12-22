class Solution:
    '''
    we process based on BODMAS and process only when we
    have a * or / operator
    '''
    def calculate(self, s: str) -> int:
        num = 0
        lastSign = '+'
        stack = []
        for i in range(0,len(s)):
            if s[i].isnumeric():
                num = num*10 + int(s[i])
            if (s[i] != " " and not s[i].isnumeric() or i == len(s)-1):
                if lastSign == '+':
                    stack.append(num)
                elif lastSign == '-':
                    stack.append(-num)
                elif lastSign == '*':
                    stack.append(stack.pop() * num)
                elif lastSign == '/':
                    stack.append(int(stack.pop() / num))
                    
                lastSign = s[i]
                num = 0
        
        res_num = 0
        while stack:
            res_num += stack.pop()
            
        return res_num