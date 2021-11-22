def primeProducts(string):
    '''
    reduces the time complexity involved in sorting the string from nk(log k) to nk
    '''
    res = 1
    primeNum = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]
    for each in string:
        res = res * primeNum[ord(each)-ord('a')]
    return res

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if(len(strs) == 0):
            return []
        anagramsDict = {}
        for each in strs:
            stringPrimeProduct = primeProducts(each)
            if(stringPrimeProduct not in anagramsDict.keys()):
                anagramsDict[stringPrimeProduct] = [each]
            else:
                anagramsDict[stringPrimeProduct].append(each)
        return anagramsDict.values()


# class Solution:
'''
here with sorting
'''
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
#         myDict = {}
#         finalList = []
        
#         for val in strs:
            
            
#             sortedVal = ''.join(sorted(val))
            
            
#             if sortedVal not in myDict:
                
#                 myDict[sortedVal] = [val]
                
                
#             else:
                
#                 myDict[sortedVal].append(val)
               
            
       
#        return myDict.values()
        