class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        '''
        in order to do an implace operation we replace every 
        1  -->  0  --> 2
        0  -->  1  --> 3
        once replaced we check on the mat again replace it with the right value
        '''
        if len(board) == 0 :return 0
        
        m = len(board)
        n = len(board[0])
        
        for i in range(m):
            for j  in range(n):
                lives = self.countLives(board, i , j)
                
                if board[i][j] == 1 and (lives < 2 or lives > 3): 
                    board[i][j] = 2
                if board[i][j] == 0 and lives == 3:
                    board[i][j] = 3
                
        for i in range(m):
            for j  in range(n):   
                if board[i][j] == 2:
                    board[i][j] = 0
                if board[i][j] == 3:
                    board[i][j] = 1
                    

    
    def countLives(self, board, i , j):
        #dirs is a direction array which has all possible directions we can move from an element
        dirs = [[-1,0],[0,1],[1,0],[0,-1],[-1,1],[1,1],[1,-1],[-1,-1]]
        count = 0
        for d in dirs:
            r = i + d[0]
            c = j + d[1]
            if (r>=0 and c>=0 and r<len(board)  and c<len(board[0])) and (board[r][c] == 1 or board[r][c] == 2):
                count +=1
     
        return count