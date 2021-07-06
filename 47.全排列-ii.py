#
# @lc app=leetcode.cn id=47 lang=python
#
# [47] 全排列 II
#

# @lc code=start
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        visited = [False] * len(nums)  # 控制子节点不能重复
        
        def backtrace(nums, path):
            repeat = []  # 控制当前层不能重复, 这里也可以先对数组进行排序，然后去重
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            for i in range(len(nums)):
                if nums[i] in repeat or visited[i] == True:
                    continue
                
                path.append(nums[i])
                repeat.append(nums[i])
                visited[i] = True
                backtrace(nums, path)
                path.pop()
                visited[i] = False

        backtrace(nums, [])
        return result


    def permuteUnique0(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        visited = [False] * len(nums)  # 控制子节点不能重复
        
        def backtrace(nums, path):
            if len(path) == len(nums):
                result.append(path[:])
                return
            
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1] and visited[i-1] == False:  # 控制当前层不能重复
                    continue
                
                if visited[i] == False:
                    path.append(nums[i])
                    visited[i] = True
                    backtrace(nums, path)
                    path.pop()
                    visited[i] = False
        
        nums = sorted(nums)  # 数组必须有序
        backtrace(nums, [])
        return result


if __name__ == '__main__':
    nums = [1,1,1,2]
    print(Solution().permuteUnique(nums))
            

# @lc code=end

