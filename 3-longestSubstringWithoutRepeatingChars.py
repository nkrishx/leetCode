class Solution:
    '''
    sliding window solution
    we keep adding into hash map where we have seen the element
    and once we see the element again then we move the window
    to index next to the repeated element, so when adding an elment into 
    the hash map we add its index+1, so that we can move the low
    to this place and skip the repeated element
    '''
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        hashMap ={}
        maxLen = 0
        low = 0
        for i in range(0,len(s)):
            if s[i] in hashMap:
                low = max(hashMap[s[i]],low)
            hashMap[s[i]] = i+1
            maxLen = max(maxLen,i-low+1)
        
        return maxLen
        