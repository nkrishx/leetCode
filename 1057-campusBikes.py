class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        if len(workers) == 0 or len(bikes) == 0:
            return 0
        
        hashMap = {}
        b = [False for each in range(0,len(bikes))]
        w = [-1 for each in range(0,len(workers))]
        count = 0
        
        for i in range(0,len(workers)):
            for j in range(0,len(bikes)):
                distance = abs(workers[i][0] - bikes[j][0]) + abs(workers[i][1] - bikes[j][1])
                if distance not in hashMap:
                    hashMap[distance] = []
                hashMap[distance].append([i,j])
        
        #print(hashMap)
        #we need to sort according to the distances, whjich is the key in hashmap
        hashMap = dict(sorted(hashMap.items()))
        #print(hashMap)
        
        for key,val in hashMap.items():
            for each in val:
                if w[each[0]] == -1 and b[each[1]] == False:
                    w[each[0]] = each[1]
                    b[each[1]] = True
                    count +=1
                if count == len(w):
                    return w
                    #break
        return w
        