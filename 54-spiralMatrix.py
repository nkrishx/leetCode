class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        '''
        maintaing 4 pointer fro up row[0][0], down[m-1][0] left[0][0], 
        right[0][n-1], initially and squeeze the bounds every iteration of while loop
        Check the base while condition inside as well, since we are altering the pointers inside the loop
        '''
        if len(matrix)  == 0: return []
        m = len(matrix)
        n = len(matrix[0])
        result = []
        left, right = 0, n-1
        up, down = 0, m-1
  
        
        while(up<=down and left<=right):
            
            if up<=down and left<=right:
                for j in range(left,right+1):
                    result.append(matrix[up][j])
                up+=1
                
            if up<=down and left<=right:
                for j in range(up, down+1):
                    result.append(matrix[j][right]) 
                right-=1
                
            if up<=down and left<=right:
                for j in range(right, left-1, -1):
                    result.append(matrix[down][j])  
                down-=1
            
            if up<=down and left<=right:
                for j in range(down, up-1, -1):
                    result.append(matrix[j][left])  
                left+=1
                
        return result