class Solution:
    '''
    bfs solution with rearrangement, making matrix into 1d array
    we need to move from left to right when in even rows and left to right when in odd
    '''
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        m = len(board)
        moves = [0] * m * m
        
        idx = 0
        i = m -1
        j = 0
        even = 0 
        
        while i>=0 and j>=0:
            if board[i][j] == -1:
                moves[idx] = -1
            else:
                moves[idx] = board[i][j] - 1
            idx+=1
            
            if even % 2 == 0:
                j += 1
            else:
                j -=1
                
            if j>m-1:
                i -= 1
                j -= 1
                even += 1
            
            if j<0:
                j+=1
                i -= 1
                even += 1
        
        queue = collections.deque()
        if moves[0]==-1:
            queue.append(0)
        else:
            queue.append(moves[0])
        
        minVal=0
        moves[0]=-2
        
        while(len(queue)!=0):
            size=len(queue)
            for k in range(0,size):
                curr=queue.popleft()
                if curr==len(moves)-1:
                    return minVal
                for l in range(1,7):
                    child=curr+l
                    if child<=len(moves)-1 and moves[child]!=-2:
                        if moves[child]==-1:
                            queue.append(child)
                        else:
                            # if moves[child]==len(moves)-1:
                            #     return minVal+1
                            # else:
                                queue.append(moves[child])
                        moves[child]=-2
            minVal+=1
        
        return -1
                                
                