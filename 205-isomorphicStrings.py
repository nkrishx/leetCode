class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        self.smap={}
        self.tmap={}
        if(len(self.smap) != len(self.tmap)):
            return False
        for each in range(0,len(s)):
            schar = s[each]
            tchar = t[each]
            if(schar in self.smap.keys()):
                if(self.smap[schar] != tchar):
                    return False
            else:
                self.smap[schar] = tchar
            if(tchar in self.tmap.keys()):
                if(self.tmap[tchar] != schar):
                    return False
            else:
                self.tmap[tchar] = schar
        return True
        