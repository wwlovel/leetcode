class Solution(object):
    def maxSubArray2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curr_sum, max_sum = nums[0],nums[0]
        for i in range(1,len(nums)):
            curr_sum = max(nums[i], curr_sum + nums[i])
            max_sum = max(max_sum, curr_sum)
        return max_sum
    def maxSubArray(self, nums):
        max_sum = nums[0]
        for i in range(1,len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
            max_sum = max(max_sum, nums[i])
        return max_sum

test = [-2,1,-3,4,-1,2,1,-5,4]
a = Solution()
print(a.maxSubArray(test))