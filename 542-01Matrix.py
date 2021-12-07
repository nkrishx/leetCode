class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        '''
        bfs solution with dirs array
        we mutate the matrix inplace to avoid the case of a node being visited 
        multiple from different nodes and adding it to the queue.
        This avoids the case for maintaining a visted array for a node
        We start with 0 as independent nodes and change all 1's to -1's
        then on each pass of the level we convert the visited node if -1 to
        the distance in that level
        '''
        if len(mat) == 0:
            return []
        
        m = len(mat)
        n = len(mat[0])
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        queue = collections.deque()
        
        #add all independent nodes (0's here) to queue first
        for i in range(0,m):
            for j in range(0,n):
                if mat[i][j] == 0:
                    queue.append([i,j])
                else:
                    mat[i][j] = -1
        
        distance = 1 #initial distance as 1
        
        while(len(queue)!=0):
            size = len(queue)
            
            for i in range(0,size):
                curr = queue.popleft()
                for each in dirs:
                    r = curr[0] + each[0]
                    c = curr[1] + each[1]
                    
                    if r >=0 and r<m and c>=0 and c<n and mat[r][c] == -1:
                        mat[r][c] = distance
                        queue.append([r,c])
            
            distance += 1
            
        return mat
            