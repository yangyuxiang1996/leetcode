#
# @lc app=leetcode.cn id=739 lang=python
#
# [739] 每日温度
#

# @lc code=start
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        if len(temperatures) == 1:
            return [0]

        res = [0]*len(temperatures)
        stack = []  # 单调递减栈，保存索引
        for i in range(len(temperatures)):
            while stack != [] and temperatures[i] >temperatures[stack[-1]]:
                idx = stack.pop()
                res[idx] = i - idx
            stack.append(i)

        return res


if __name__ == '__main__':
    temperatures = [73,74,75,71,69,72,76,73]
    print(Solution().dailyTemperatures(temperatures))
# @lc code=end