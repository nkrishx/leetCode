class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations)==0:
            return 0
        
        citations.sort()
        for i in range(0,len(citations)):
            diff=len(citations)-i
            if citations[i] >= diff:
                return diff
            
        return 0
        