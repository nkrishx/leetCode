class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        '''
        backtracking with some optimizations
        we traverse row by row and when checking for the validity of 
        placing a queen we look up only till the row we are currently at 
        this is since for a given row,column we don't need to check 
        anything below it row and column wise and also diagonally
        n! time complexity since every successive row we reduce options by factorial pattern
        '''
        self.board = [[0 for i in range(n)] for j in range(n)] 
        #create a board of n*n dimension
        #note do not create a matrix using this pattern [[0]*n]*n since this will be a memory 
        #reference and any change in values like board[0][0]=1 will cause board[1][0] and all         
        #other rows with 0th column to be chnages 
        self.result = []
        self.m = n
        
        self.backTrack(0) #we start backtracking with first row, can be done as column too
        return self.result
    
    def backTrack(self,r):
        #base
        if r==self.m:#valid case where we have successfully covered all rows
            li =[]
            for i in range(0,self.m):
                s = ""
                for j in range(0,self.m):
                    if self.board[i][j] == 1:
                        s = s+"Q"
                    else:
                        s = s+"."
                li.append(s)
            self.result.append(li)
            return
            
        #logic
        for j in range(0,self.m): # we only look till the row we are at and 
            print r,j
            if self.isSafe(r,j):  #we need to go over eachcolumn
                #action
                print self.board
                print r,j
                self.board[r][j] = 1 
                print self.board
                #recuse
                self.backTrack(r+1)
                #backtrack
                self.board[r][j] = 0  
    
    def isSafe(self, r, c):
        '''
        use to check if we can put in the given row col
        we check only until the current row we have come and similarly for the diagonals too 
        '''
        #column above
        for k in range(0,r):
            if self.board[k][c] == 1:
                return False
        
        #diagonal left
        i=r
        j=c
        while(i>=0 and j>=0):
            if self.board[i][j] == 1:
                return False
            i = i-1
            j = j-1
            
        #diagonal right
        i=r
        j=c
        while(i>=0 and j<self.m):
            if self.board[i][j] == 1:
                return False
            i = i-1
            j = j+1
        return True