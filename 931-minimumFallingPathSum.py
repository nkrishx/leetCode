class Solution:
    #commented recursive approach
    #dp solution by mutating the given matrix, bottom up approach(starting from the bottom)
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        for i in range(len(matrix)-2,-1,-1):
            for j in range(0,len(matrix[i])):
                if j == 0:
                    matrix[i][j] = matrix[i][j] + min(matrix[i+1][j],matrix[i+1][j+1])
                elif j == len(matrix[i])-1:
                    matrix[i][j] = matrix[i][j] + min(matrix[i+1][j],matrix[i+1][j-1])
                else:
                    matrix[i][j] = matrix[i][j] + min(matrix[i+1][j],matrix[i+1][j+1],matrix[i+1][j-1])
        
        print(matrix)
        return min(matrix[0])
                    
        
#         minSum = sys.maxsize
#         result = [0 for each in range(0,len(matrix[0]))]
#         for j in range(0,len(matrix[0])):
#             result[j] = min(minSum,self.helper(matrix,0,j,0))
        
#         print(result)
#         return min(result)
            
#     def helper(self,matrix,row,col,s):
#         #base
#         if row == len(matrix):
#             return s
        
#         #logic
#         if col == 0:
#             return min(self.helper(matrix,row+1,col,s+matrix[row][col]), self.helper(matrix,row+1,col+1,s+matrix[row][col]))
#         elif col == len(matrix[0])-1:
#             return min(self.helper(matrix,row+1,col,s+matrix[row][col]), self.helper(matrix,row+1,col-1,s+matrix[row][col]))
#         else:
#             return min(self.helper(matrix,row+1,col,s+matrix[row][col]), self.helper(matrix,row+1,col+1,s+matrix[row][col]), self.helper(matrix,row+1,col-1,s+matrix[row][col]))