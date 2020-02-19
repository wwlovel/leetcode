class Solution(object):
    def isPalindrome1(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        n = len(s)
        i = 0
        j = n-1
        while(i<j):
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if (x < 0):
            return False
        if (x%10 == 0 and x!= 0):
            return False

        rev = 0
        while(x>rev):
            rev = rev*10 + x%10
            x = int(x/10)
        return x==rev or x== int(rev/10)


t = Solution()
test = 10
print(t.isPalindrome(test))