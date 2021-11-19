class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        self.matrix = matrix
        self.target = target
        if len(self.matrix)==0:
            return False
        self.low = 0
        self.high = len(self.matrix[0]) * len(self.matrix) - 1 
        self.n = len(matrix[0])
        
        while(self.low<=self.high):
            mid = self.low + (self.high-self.low)/2
            r = mid / self.n
            c = mid % self.n
            if matrix[r][c] == self.target:
                return True
            elif matrix[r][c]<self.target:
                self.low = mid+1
            else:
                self.high = mid-1
        return False