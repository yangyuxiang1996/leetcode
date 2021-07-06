#
# @lc app=leetcode.cn id=376 lang=python
#
# [376] 摆动序列
#

# @lc code=start
class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        
        cur_diff = pre_diff = 0
        result = 1
        for i in range(len(nums)-1):
            cur_diff = nums[i] - nums[i+1]  # 记录当前差值
            if (cur_diff > 0 and pre_diff <= 0) or (cur_diff < 0 and pre_diff >= 0):
                result += 1
                pre_diff = cur_diff

        return result

if __name__ == '__main__':
    nums = [1,2,3,4,5,6,7,8,9]
    print(Solution().wiggleMaxLength(nums))



# @lc code=end

