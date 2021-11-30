class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        '''
        we start at the bottom left or the top right
        this is because we get idea on which direction to move in
        since the adjacent element might be lesser or greater than it
        '''
        if(len(matrix) == 0):
            return False
        m = len(matrix)
        n = len(matrix[0])
        i = 0
        j = n-1
        while(j >=0 and i<m):
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] > target:
                j -= 1
            else:
                i += 1
        return False
            
        