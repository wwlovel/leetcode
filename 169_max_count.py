class Solution(object):
    def majorityElement1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        curr_m = nums[0]
        for i in range(len(nums)):
            if count == 0:
                curr_m = nums[i]
            if nums[i] == curr_m:
                count += 1
            else:
                count -= 1
        return curr_m
    def majorityElement(self, nums):
        d = {}
        max_count = len(nums)//2
        for i in nums:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
            if d[i] > max_count:
                return i

t = Solution()
print(t.majorityElement([2,2,1,1,1,2,2]))