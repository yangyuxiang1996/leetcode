#
# @lc app=leetcode.cn id=135 lang=python
#
# [135] 分发糖果
#

# @lc code=start
class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        # 先考虑右边孩子评分高于左边孩子的情况
        candys = [1] * len(ratings)
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i-1]:
                candys[i] = candys[i-1] + 1

        # 然后考虑左边孩子评分高于右边孩子的情况
        for i in range(len(ratings)-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candys[i] = max(candys[i], candys[i+1] + 1)

        return sum(candys)
        





# @lc code=end

