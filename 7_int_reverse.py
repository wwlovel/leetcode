class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        _min = -2147483648
        _max = 2147483647
        rs = 0
        flag = 1 if x > 0 else -1
        x = x*flag
        while(x!=0):
            rs = rs*10 + x%10
            x = int(x/10)
        return 0 if rs>_max else rs*flag

t = Solution()
test = 120
print(t.reverse(test))