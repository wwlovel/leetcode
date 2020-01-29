class Solution(object):
    def moveZeroes2(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 0:
            return nums
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        for k in range(j,len(nums)):
            nums[k] = 0
        return nums
    def moveZeroes(self, nums):
        if len(nums) <= 0:
            return nums
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1
        return nums

t = Solution()
print(t.moveZeroes([1,2,3,0,0,4,0]))