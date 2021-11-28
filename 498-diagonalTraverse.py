class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        '''
        boundary conditions are important here and the order of the conditions check inside d=1 and d=-1
        '''
        if(len(mat) == 0):
            return []
        row = len(mat)
        col = len(mat[0])
        result = [0] * (row*col)
        index = 0
        i = 0
        j = 0
        d = 1
        while(index < (row*col)):
            result[index] = mat[i][j]
            if d == 1:
                if j == col - 1:
                    i += 1
                    d = -1
                elif i == 0:
                    j += 1
                    d = -1
                else:
                    i -= 1
                    j +=1
            else:
                if i == row -1:
                    j +=1
                    d = 1
                elif j == 0:
                    i += 1
                    d = 1
                else:
                    i += 1
                    j -= 1
            index += 1
        return result
                    
                
        