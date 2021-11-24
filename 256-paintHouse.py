class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        
        if not costs:
            return 0
        cr = costs[len(costs)-1][0]
        cg = costs[len(costs)-1][1]
        cb = costs[len(costs)-1][2]
        
        for i in range(len(costs)-2,-1,-1):
            tempr = cr
            tempg = cg
            cr = costs[i][0] + min(cb, cg)
            cg = costs[i][1] + min(cb, tempr)
            cb = costs[i][2] + min(tempr, tempg)
            
        return min(cr,cb, cg)
        
        
        # for i in range(len(costs)-2,-1,-1):
            # costs[i][0] = costs[i][0]+min(costs[i+1][1],costs[i+1][2])
            # costs[i][1] = costs[i][1]+min(costs[i+1][0],costs[i+1][2])
            # costs[i][2] = costs[i][2]+min(costs[i+1][0],costs[i+1][1])
            
        # return min(costs[0][0],costs[0][1],costs[0][2])