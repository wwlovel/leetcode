class Solution(object):
    def climbStairs2(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        for i in range(3,n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
    def climbStairs(self, n):
        import math
        return (1/math.sqrt(5)) * ( math.pow(((1+math.sqrt(5))/2),n+1) - math.pow(((1-math.sqrt(5))/2),n+1))

a = Solution()
print(a.climbStairs(5))
