#给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始
# ）。如果不存在，则返回-1 。
# 输入：haystack = "hello", needle = "ll"
# 输出：2


class Solution:
    def strStr(self,haystack,needle):
        for i in haystack:
            for j in needle:
                if i==j:
                   return print(haystack.index(i))

s=Solution()
haystack=[1,2,3,4,5]
needle=[3,7,8]
s.strStr(haystack,needle)
