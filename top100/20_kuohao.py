class Solution(object):
	def isValid(self, s):
		"""
		:type s: str
		:rtype: bool
		"""
		d = {'{':'}','[':']','(':')'}
		zhan = []
		for i in range(len(s)):
			if s[i] in d:
				zhan.append(s[i])
			elif len(zhan) > 0 and d[zhan[-1]] == s[i]:
				zhan.pop()
			else:
				return False
		if len(zhan) != 0:
			return False
		return True

t = "{}"
tc = Solution()
print(tc.isValid(t))
