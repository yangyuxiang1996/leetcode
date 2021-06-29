#
# @lc app=leetcode.cn id=54 lang=python
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        
        m, n = len(matrix), len(matrix[0])
        up, down, left, right = 0, m-1, 0, n-1
        res = []
        while len(res) < m * n:
            
            for j in range(left, right+1):
                res.append(matrix[up][j])
            up += 1
            if len(res) == m*n:
                return res

            for i in range(up, down+1):
                res.append(matrix[i][right])
            right -= 1

            for j in range(right, left-1, -1):
                res.append(matrix[down][j])
            down -= 1
            if len(res) == m*n:
                return res

            for i in range(down, up-1, -1):
                res.append(matrix[i][left])
            left += 1

        return res


if __name__ == '__main__':
    matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    print(Solution().spiralOrder(matrix))

# @lc code=end

