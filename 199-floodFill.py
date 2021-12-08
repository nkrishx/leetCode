class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        '''
        can be done using bfs or dfs
        we take the given pixel as the independent node (image[sr][sc])
        convert it to the color and then iterate over the dirs and check if its the same 
        color as the given pixel was initially, if so then convert it and add to queue
        '''
        
        if len(image)==0 and image[sr][sc] == newColor:
            return image
        
        m = len(image)
        n = len(image[0])
        queue = collections.deque()
        color = image[sr][sc] #initial color for comparision
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        
        queue.append([sr,sc]) #add the index of given pixel into queue
        image[sr][sc] = newColor #convert it to the new given color
        
        while(len(queue)!= 0):
            curr = queue.popleft()
            for each in dirs:
                r = curr[0] + each[0]
                c = curr[1] + each[1]
                if r >= 0 and r < m and c >= 0 and c < n and image[r][c]==color and image[r][c]!=newColor:
                    #we add into queue only if the neighbour is the same color of the initial                       pixel given and not equal to the new color to be converted to
                    image[r][c] = newColor
                    queue.append([r,c])
        return image
        
        