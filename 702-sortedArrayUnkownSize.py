# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#    def get(self, index):
#        """
#        :type index: int
#        :rtype int
#        """

def binarySearch(reader,target,low,high):
    while(low <= high) :
        mid = low + (high - low)/2
        if(reader.get(mid) == target):
            return mid
        elif(reader.get(mid) < target):
            low = mid+1
        else:
            high = mid-1
    return -1
    

class Solution(object):
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        self.target = target
        self.reader = reader
        self.low = 0
        self.high = 1
        while(self.reader.get(self.high) < sys.maxint and self.reader.get(self.high) < self.target):
            self.low = self.high+1
            self.high = 2 * self.high
        return binarySearch(self.reader, self.target, self.low, self.high)
        