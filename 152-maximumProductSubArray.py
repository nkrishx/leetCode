class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        '''
        at any given number we have choose from 3 choices
        the current number, the previous max * current number or the previous min * current number
        '''
        if len(nums) == 0:
            return 0

        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far

        for i in range(1, len(nums)):
            curr = nums[i]
            temp_max = max(curr, max_so_far * curr, min_so_far * curr)
            min_so_far = min(curr, max_so_far * curr, min_so_far * curr)

            max_so_far = temp_max

            result = max(max_so_far, result)

        return result

        # if len(nums) == 0:
        #     return 0

        # result = -sys.maxsize

        # for i in range(len(nums)):
        #     accu = 1
        #     for j in range(i, len(nums)):
        #         accu *= nums[j]
        #         result = max(result, accu)

        # return result