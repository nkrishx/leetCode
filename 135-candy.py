class Solution:
    '''
    we can do a left traversal first and a right next
    in right we increase the candies onlt if the current candies given already by lwft is
    lesser than the candies of right neighbour+1.
    If we keep traversiong from the left we will have an n^2 kind of solutiom
    here we will have o(n) average
    '''
    def candy(self, ratings: List[int]) -> int:
        candies=[1 for i in range(0,len(ratings))]
        n=len(ratings)
        
        #left pass
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                candies[i]=candies[i-1]+1
        
        #right pass
        for i in range(n-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                candies[i]=max(candies[i],candies[i+1]+1)
        
        return sum(candies)