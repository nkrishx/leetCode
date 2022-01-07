class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        
        people.sort(key = lambda x: (-x[0], x[1]))
        #normal sort sorts in ascending but we want descending sorting for x[0] and 
        #ascending for x[1]
        
        result = []
        for val in people:
            result.insert(val[1], [val[0],val[1]])
            
        return result