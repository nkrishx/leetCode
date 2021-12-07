"""
# Definition for Employee.
class Employee(object):
    def __init__(self, id, importance, subordinates):
    	#################
        :type id: int
        :type importance: int
        :type subordinates: List[int]
        #################
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution(object):
    def __init__(self):
        self.result = 0
        self.hashMap = {}
        
    def dfs(self, id):
        curr = self.hashMap[id]
        self.result = self.result + curr.importance
        
        for subId in curr.subordinates:
            self.dfs(subId)
        
        
    def getImportance(self, employees, id):
        """
        :type employees: List[Employee]
        :type id: int
        :rtype: int
        """
        '''
        solved by dfs or bfs
        set up a hashmap for the lookup of the initial id
        don't need a size/level distinction since we are not concerned about a particular             level but all of the nodes
        commented bfs solution
        '''
        #create hashmap
        for each in employees:
            self.hashMap[each.id] = each
            
        #call dfs on the search id
        self.dfs(id)
        return self.result
        
#         result = 0
#         hashMap = {}
#         queue = collections.deque()
        
#         #create hashmap
#         for each in employees:
#             hashMap[each.id] = each
            
#         #add the id of the search employee to queue
#         queue.append(id)
        
        
#         while(len(queue)!=0):
#             curr = queue.popleft()
#             result = result + hashMap[curr].importance
            
#             for subId in hashMap[curr].subordinates:
#                 queue.append(subId)
                
#         return result
        