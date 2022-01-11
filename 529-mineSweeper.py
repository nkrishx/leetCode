class Solution:
    '''
    bfs solution
    '''
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        self.m=len(board)
        self.n=len(board[0])
        
        self.dirs=[[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]
        if board[click[0]][click[1]]=='M':
            board[click[0]][click[1]]='X'
            return board
        
        queue=collections.deque()
        queue.append(click)
        board[click[0]][click[1]]='B'
        
        while(len(queue)!=0):
            curr=queue.popleft()
            mines = self.getMines(board,curr[0],curr[1])
            print(mines)
            if mines==0:
                for each in self.dirs:
                    row=curr[0]+each[0]
                    col=curr[1]+each[1]
                    if row >=0 and row <self.m and col >=0 and col <self.n and board[row][col]=='E':
                        board[row][col]='B'
                        queue.append([row,col])
            else:
                board[curr[0]][curr[1]]=str(mines)
            
        return board
    
    def getMines(self,board,i,j):
        result=0
        for each in self.dirs:
            r=i+each[0]
            c=j+each[1]
            if r>=0 and r<self.m and c>=0 and c<self.n and board[r][c]=='M':
                result+=1
        
        return result
                    