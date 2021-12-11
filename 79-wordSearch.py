class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        '''
        dfs and backtracking solution, 
        we mutate the matrix elements inplace to cover the case of same element 
        visited multiple times
        '''
        if(len(board) ==0):
            return False
        self.dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        self.m = len(board)
        self.n = len(board[0])
        
        for i in range(0,self.m):
            for j in range(0,self.n):
                if self.backTrack(board,word,i,j,0): #board,word,i,j,index of word
                    return True
        return False
    
    def backTrack(self,board,word,i,j,index):
        #base
        if index==len(word):
            return True
        if i == self.m or j == self.n or i < 0 or j < 0 or board[i][j] == '#':
            return False

        #logic
        #action
        if board[i][j] == word[index]:
            temp = board[i][j]
            board[i][j] = "#"
            #recurse
            for each in self.dirs:
                r = each[0] + i
                c = each[1] + j
                if self.backTrack(board,word,r,c,index+1):
                    return True
            #backtrack
            board[i][j] = temp
        return False
        