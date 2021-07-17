#
# @lc app=leetcode.cn id=139 lang=python
#
# [139] 单词拆分
#

# @lc code=start
class Solution(object):
    def wordBreak0(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        完全背包问题
        """
        n = len(s)

        dp = [False for _ in range(n+1)]
        dp[0] = True
        for j in range(1, n+1):
            for i in range(len(wordDict)):
                if j - len(wordDict[i]) >= 0 and s[j-len(wordDict[i]):j] == wordDict[i]:
                    dp[j] = dp[j] or dp[j-len(wordDict[i])]
        print(dp)
        return dp[-1]

    
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        回溯，暴搜, 超时
        """
        def backtrace(s, wordDict, start, tmp):
            if len("".join(tmp)) > len(s):
                return
            if "".join(tmp) == s:
                return True
            
            for i in range(len(wordDict)):
                tmp.append(wordDict[i])
                if backtrace(s, wordDict, start, tmp):
                    return True
                tmp.pop()
            
            return False
        
        return backtrace(s, wordDict, 0, [])


if __name__ == '__main__':
    s = "catsandog"
    wordDict = ["cats", "dog", "sand", "and", "cat"]
    print(Solution().wordBreak(s, wordDict))
                
            
# @lc code=end

