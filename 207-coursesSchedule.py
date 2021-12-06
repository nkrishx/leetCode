class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        '''
        graph problem, we need to find independent nodes first
        the nodes are actually the elements in the prerequisite
        we mainatain an indegree list here, meaning for each node how many edges are coming in
        we maintain a hash map for each node which all nodes it affects
        we add to a que who's indegree value is 0, meaning it has no dependency on other nodes
        or its prerequisites have been completed
        '''
        if not numCourses:
            return False
        
        dependency = {}
        inbound = [0]*numCourses
        
        for val in prerequisites:
            
            if val[1] not in dependency:
                dependency[val[1]] = [] #set empty list since a node can be prerequisite for many nodes
            
            dependency[val[1]].append(val[0])
            inbound[val[0]] += 1 #increment the indgree for the node if it is dependent on the current prerequisite
            
        count = 0 
        queue = deque() #we can use a list too
        
        
        for i in range(len(inbound)): #add all independent nodes first into the queue
            if inbound[i] == 0:
                queue.append(i)
        
        
        while queue:
            count += 1
            curr = queue.pop()
            if dependency.get(curr):
            
                for val in dependency.get(curr):
                    inbound[val] -= 1 #decrement the indegree of each item for this particular node, meaning the current prerequisite for the node is done 
                    if inbound[val] == 0:
                        queue.append(val)
                    
        if count == numCourses:
            return True
        
        return False
        