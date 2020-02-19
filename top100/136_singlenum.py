class Solution(object):
    def singleNumber2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = 0
        for i in nums:
            a ^= i
        return a
    def singleNumber(self, nums):
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d.pop(i)
        return d.popitem()[0]

t = Solution()
print(t.singleNumber([4,1,2,1,2]))