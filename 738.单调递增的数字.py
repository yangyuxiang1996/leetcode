#
# @lc app=leetcode.cn id=738 lang=python
#
# [738] 单调递增的数字
#

# @lc code=start
class Solution(object):
    def monotoneIncreasingDigits(self, n):
        """
        :type n: int
        :rtype: int
        从后往前遍历
        """
        if n < 10:
            return n
        nl = list(str(n))
        for i in range(len(nl)-1, 0, -1):
            if nl[i-1] > nl[i]:
                nl[i-1] = str(int(nl[i-1])-1)
                nl[i:] = ['9'] * len(nl[i:])
        return int("".join(nl))


    def monotoneIncreasingDigits0(self, n):
        """
        :type n: int
        :rtype: int
        从前往后遍历
        """
        if n < 10:
            return n
        nl = list(str(n))
        for i in range(len(nl)-1):
            if int(nl[i]) > int(nl[i+1]):
                nl[i] = str(int(nl[i])-1)
                for j in range(i+1, len(nl)):
                    nl[j] = '9'
                # 往前判断
                j = i
                while j > 0 and nl[j-1] > nl[j]:
                    nl[j-1] = str(int(nl[j-1])-1)
                    nl[j] = '9'
                    j -= 1
        res = int("".join(nl))
        return res


if __name__ == '__main__':
    n = 99998
    print(Solution().monotoneIncreasingDigits(n))

            


# @lc code=end

