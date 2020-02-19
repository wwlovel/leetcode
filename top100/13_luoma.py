class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        d = {'I':1,
             'V':5,
             'X':10,
             'L':50,
             'C':100,
             'D':500,
             'M':1000
             }
        r = 0
        zhan = []
        for i in range(len(s)):
            if len(zhan) > 0 and zhan[-1] > 0 and zhan[-1] < d[s[i]]:
                a = -zhan[-1]-zhan[-1]
                r += a
                zhan.append(a)
            r += d[s[i]]
            zhan.append(d[s[i]])
        return r

t = Solution()
print(t.romanToInt('IX'))
