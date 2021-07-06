#
# @lc app=leetcode.cn id=40 lang=python
#
# [40] 组合总和 II
#

# @lc code=start
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []
        candidates = sorted(candidates)  # 先排序，使得相同的数挨在一起
        demo = [False] * len(candidates)  # 第一种去重方法，定义一个全局数组保存当前元素是否使用过

        def backtrace(start, path, target, result):
            if result > target:
                return
            if result == target:
                self.res.append(path[:])
            
            repeat = []  # 第二种去重方法，在每一层初始化一个数组，记录当前层出现过的元素
            for i in range(start, len(candidates)):
                # if i > 0 and candidates[i] == candidates[i-1] and demo[i-1] == False:  # 树层重
                #     continue
                if candidates[i] in repeat:
                    continue
                repeat.append(candidates[i])
                result += candidates[i]
                path.append(candidates[i])
                demo[i] = True
                backtrace(i+1, path, target, result)
                result -= candidates[i]
                path.pop() 
                demo[i] = False
                

        backtrace(0, [], target, 0)
        return self.res


if __name__ == '__main__':
    candidates = [10,1,2,7,6,1,5]
    target = 8
    print(Solution().combinationSum2(candidates, target))
# @lc code=end

