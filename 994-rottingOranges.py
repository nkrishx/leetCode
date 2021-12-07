class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        '''
        bfs solution, we consider already rotted oranges as independent nodes and 
        start processing from there. Add rotten into queue every level
        get initial counts of all fresh and then for each rotten orange rot the 
        adjacent oranges in 4 directions using dirs array.
        Check if fresh is 0 once all of the elements in the queue is processed
        if not then all oranges cannot be rotten.
        Time would be overall time-1 since we incrent time after procesing the last level too
        '''
        m = len(grid)
        n = len(grid[0])
        fresh = 0
        time = 0
        queue = collections.deque()
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        
        for i in range(0,m):
            for j in range(0,n):
                if grid[i][j] == 2:
                    queue.append([i,j])
                elif grid[i][j] == 1:
                    fresh += 1
                
        if fresh == 0:
            return 0
        
        while(len(queue) !=0 ):
            size = len(queue)
            for i in range(0,size):
                curr = queue.popleft()
                for each in dirs:
                    r = each[0] + curr[0]
                    c = each[1] + curr[1]

                    if r >=0 and r < m and  c>=0 and c<n and grid[r][c] == 1: #fresh
                        queue.append([r,c])
                        grid[r][c] = 2
                        fresh -= 1
            
            time += 1 #increment time for each level
            
        if fresh == 0:
            return time-1
        else:
            return -1
            
        
        