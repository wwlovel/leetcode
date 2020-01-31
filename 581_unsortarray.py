class Solution(object):
    def findUnsortedSubarray2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        a = nums.copy()
        a.sort()
        start = len(a)
        end = 0
        for i in range(len(a)):
            if a[i] != nums[i]:
                start = min(start, i)
                end = max(end, i)
                print(i, start, end)
        return end-start+1 if end-start+1 >= 0 else 0

    def findUnsortedSubarray(self, nums):
        #right
        _max = nums[0]
        right = -1
        for i in range(len(nums)):
            if nums[i] >= _max:
                _max = nums[i]
            else:
                right = i
        print(right)
        _min = nums[-1]
        left = 0
        for j in range(len(nums)-1, -1, -1):
            if nums[j] <= _min:
                _min = nums[j]
            else:
                left = j
        print(left)
        return right-left+1 if right-left+1>=0 else 0


t = Solution()
print(t.findUnsortedSubarray([5,6,7,8]))
