class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pStar = -1
        sStar = -1
        pp = 0
        sp = 0
        
        while sp < len(s):
            
            if pp < len(p) and (s[sp] == p[pp] or p[pp] == '?'):
                sp += 1
                pp += 1
            
            elif pp < len(p) and p[pp] == '*':
                sStar = sp
                pStar = pp
                pp += 1
            
            elif pStar == -1:
                return False
            
            else:
                sStar += 1
                sp = sStar
                pp = pStar + 1
        
        
        while pp < len(p):
            
            if p[pp] != '*':
                return False
            pp += 1
        
        return True