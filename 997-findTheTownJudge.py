class Solution:
    '''
    graph based problem when drawn out
    so we can build an indgrees array and work on that
    for a judge to exist we need to make sure there is an indegree
    which is equal to N-1 meaning everyone trusts the person and the person trusts no one
    Note: person array run from 1-N and indgrees from 0
    we increase the indgree of a person if trusted by someone and decresease the indegree
    of the person who trusts someone
    '''
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        indegrees=[0 for each in range(0,n)]
        
        for i in trust:
            indegrees[i[0]-1]-=1
            indegrees[i[1]-1]+=1
        
        for i in range(0,n):
            if indegrees[i] == n-1:
                return i+1
        
        return -1