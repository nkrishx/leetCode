class Solution(object):
    # def dfs(self,grid,i,j):
    #     if(i<0 or i==self.m or j<0 or j==self.n or grid[i][j] !='1'):
    #         return
    #     grid[i][j] = '0'
    #     for each in self.dirs:
    #         r = each[0] + i
    #         c = each[1] + j
    #         self.dfs(grid,r,c)
            
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        '''
        bfs solution,
        check for an element to be 1, add it to queue and make it 0
        so that if encountered from different element it is already marked as visited previously
        commented dfs solution
        '''
        if(len(grid) == 0):
            return 0
        self.m = len(grid)
        self.n = len(grid[0])
        self.dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        self.queue = collections.deque()
        self.count = 0
        
        for i in range(0,self.m):
            for j in range(0,self.n):
                if grid[i][j] == '1':
                    self.count +=1
                    # self.dfs(grid,i,j)
                    self.queue.append([i,j])
                    grid[i][j] = 0
                    while(len(self.queue)!=0):
                        curr = self.queue.popleft()
                        for each in self.dirs:
                            r = curr[0] + each[0]
                            c = curr[1] + each[1]
                            if r >=0 and r<self.m and c>=0 and c<self.n and grid[r][c] == '1':
                                self.queue.append([r,c])
                                grid[r][c] = 0
        return self.count
    
    
            