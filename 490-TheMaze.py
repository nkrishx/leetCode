class Solution:
    '''
    dfs and bfs solution possible here
    we need to modify such that when we move in directions array
    we dont move to the immediate neighbour but we need to stop at 
    the point where we touch the wall or a hurdle.
    We need to mark any cell visited as well
    dfs solution commented
    '''
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        if len(maze)==0:
            return False
        
        m = len(maze)
        n = len(maze[0])
        
        dirs = [[0,1],[1,0],[-1,0],[0,-1]]
        queue = collections.deque()
        
        queue.append([start[0],start[1]])
        maze[start[0]][start[1]] = 2
        
        while(len(queue)!=0):
            curr=queue.popleft()
            if curr[0]==destination[0] and curr[1]==destination[1]:
                return True
            
            for d in dirs:
                i = curr[0]
                j = curr[1]
                
                while(i<m and j<n and i>=0 and j>=0 and maze[i][j]!=1):
                    i=i+d[0]
                    j=j+d[1]
                
                #we break the while condition on meeting the wall or hurdle
                #we need to add the cell before it to mark as visited
                i=i-d[0]
                j=j-d[1]
                
                if maze[i][j] != 2:
                    queue.append([i,j])
                    maze[i][j] = 2
        
        
        return False

    #     def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
    #     self.dirs = [[0,1],[1,0],[-1,0],[0,-1]]
    #     return self.dfs(maze, start, destination)
        
        
    # def dfs(self, maze, curr, destination):
        
    #     if maze[curr[0]][curr[1]] == 2:
    #         return False
        
        
    #     if curr[0] == destination[0] and curr[1] == destination[1]:
    #         return True
    #     maze[curr[0]][curr[1]] = 2
    #     for d in self.dirs:
    #         i = curr[0]
    #         j = curr[1]
    #         while i>= 0 and j>= 0 and i<len(maze) and j<len(maze[0]) and maze[i][j] != 1:
    #             i += d[0]
    #             j += d[1]
            
    #         i -= d[0]
    #         j -= d[1]
            
    #         if self.dfs(maze, [i,j], destination):
    #             return True
            
            
    #     return False