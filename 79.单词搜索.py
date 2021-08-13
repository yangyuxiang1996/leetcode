#
# @lc app=leetcode.cn id=79 lang=python
#
# [79] 单词搜索
#

# @lc code=start
class Solution(object):
    def __init__(self):
        self.directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m, n = len(board), len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if self.backtrace(board, word, i, j, visited, 0):
                    return True
        return False
    
    def backtrace(self, board, word, row, col, visited, k):
        m, n = len(board), len(board[0])
        if board[row][col] != word[k]:
            return False
        if k == len(word)-1:
            return True

        visited[row][col] = True
        for direction in self.directions:
            i, j = direction[0], direction[1]
            new_row, new_col = row + i, col + j
            if new_row >= 0 and new_col >= 0 and new_row < m and  new_col < n: 
                if visited[new_row][new_col] == False:
                    # print(new_row, new_col)
                    flag = self.backtrace(board, word, new_row, new_col, visited, k+1)
                    if flag:
                        return True
        visited[row][col] = False
        return False

if __name__ == '__main__':
    board = [["C","A","A"],["A","A","A"],["B","C","D"]]
    word = "AAB"
    print(Solution().exist(board, word))
# @lc code=end

