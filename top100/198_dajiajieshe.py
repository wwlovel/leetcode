class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = [0]*(len(nums)+2)
        for i in range(len(nums)):
            l[i+2] = max(l[i] + nums[i], l[i+1])
        return l[-1]
t = Solution()
print(t.rob([2,7,9,3,1]))