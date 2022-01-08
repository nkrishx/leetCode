class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expectedSum=0
        actualSum=0
        n=1
        for each in nums:
            actualSum+=each
            expectedSum+=n
            n+=1

        num=expectedSum-actualSum
        return num