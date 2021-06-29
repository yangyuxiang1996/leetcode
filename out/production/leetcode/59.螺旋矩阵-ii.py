#
# @lc app=leetcode.cn id=59 lang=python
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if not n:
            return []
        
        up, down, left, right = 0, n-1, 0, n-1
        step = 1
        matrix = [[0] * n for _ in range(n)]
        while step <= n*n:
            for j in range(left, right+1):
                matrix[up][j] = step
                step += 1
            up += 1
            for i in range(up, down+1):
                matrix[i][right] = step
                step += 1
            right -= 1
            for j in range(right, left-1, -1):
                matrix[down][j] = step
                step += 1
            down -= 1
            for i in range(down, up-1, -1):
                matrix[i][left] = step
                step += 1
            left += 1

        return matrix




    def generateMatrix0(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if not n:
            return []
        
        matrix = [[0 for _ in range(n)] for _ in range(n)]
        # matrix[0][0] = 1
        startx = starty = 0
        step = 1
        loop = n / 2  # 每个圈循环几次，例如n为奇数3，那么loop = 1 只是循环一圈，矩阵中间的值需要单独处理
        mid = n / 2  # n为奇数时中间的值要单独处理
        offset =  1  # 每一圈循环，需要控制每一条边遍历的长度
        while loop > 0:
            i, j = startx, starty
            while j < starty + n - offset:
                matrix[i][j] = step
                step += 1
                j += 1
            while i < startx + n - offset:
                matrix[i][j] = step
                step += 1
                i += 1
            while j > starty:
                matrix[i][j] = step
                step += 1
                j -= 1
            while i > startx:
                matrix[i][j] = step
                step += 1
                i -= 1

            startx += 1
            starty += 1
            offset += 2
            loop -= 1

        if n % 2 == 1:
            matrix[mid][mid] = step

        return matrix





# @lc code=end

