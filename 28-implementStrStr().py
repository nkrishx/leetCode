class Solution:
    '''
    uses knp algo with sliding window
    we make a lps(longest prefix suffix) array for the given input
    use the lps array for comparing the needle with the haystack
    note, we never move the i pointer back but only the j
    '''
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle)==0:
            return 0
        
        lps_array=self.lps(needle)
        m=len(haystack)
        n=len(needle)
        i=0
        j=0
        while(i<m):
            if needle[j]==haystack[i]:
                i+=1
                j+=1
                if j==n:
                    return i-n
            elif j>0 and needle[j]!=haystack[i]:
                j=lps_array[j-1]
            elif j==0 and needle[j]!=haystack[i]:
                i+=1
        return -1
        
    def lps(self,needle):
        n = len(needle)
        lps=[0]*len(needle)
        lps[0]=0
        i = 1
        j = 0
        while(i < n):
            if needle[i]==needle[j]:
                j+=1
                lps[i]=j
                i+=1
            elif j>0 and needle[i]!=needle[j]:
                j=lps[j-1]
            elif j==0 and needle[i]!=needle[j]:
                i+=1
        return lps
                