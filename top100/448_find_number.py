class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            new_index = abs(nums[i]) -1
            if nums[new_index] > 0:
                nums[new_index] *= -1
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i+1)
        return result
t = Solution()
print(t.findDisappearedNumbers([3,3,3,1,4,5,6,4]))