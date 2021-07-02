#
# @lc app=leetcode.cn id=216 lang=python
#
# [216] 组合总和 III
#

# @lc code=start
class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        回溯法，注意浅拷贝深拷贝问题
        """
        if k == 0 or n == 0:
            return []
        
        self.res = []

        def backtrace(n, k, start, path):
            if len(path) == k:
                if sum(path) != n:
                    return
                else:
                    self.res.append(path[:])
             
            end = min(n-sum(path), 9)
            for i in range(start, end + 1):
                path.append(i)
                backtrace(n, k, i+1, path)
                path.pop()
        
        backtrace(n, k, 1, [])
        return self.res

    
if __name__ == '__main__':
    k, n = 2, 18
    print(Solution().combinationSum3(k, n))

# @lc code=end

