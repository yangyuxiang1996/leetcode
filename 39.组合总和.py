#
# @lc app=leetcode.cn id=39 lang=python
#
# [39] 组合总和
#

# @lc code=start
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []
        
        self.res = []
        def backtrace(candidates, path, target, tmp):
            if tmp > target:
                return
            if tmp == target:
                self.res.append(path[:])
            
            for i in range(len(candidates)):
                candidate = candidates[i]
                tmp += candidate
                path.append(candidate)
                backtrace(candidates[i:], path, target, tmp)
                tmp -= candidate
                path.pop()

        backtrace(candidates, [], target, 0)
        return self.res

# @lc code=end

