#
# @lc app=leetcode.cn id=93 lang=python
#
# [93] 复原 IP 地址
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        if len(s) > 1 and s[0] == "0":
            return False
        if 0 <= int(s) <= 255:
            return True
        return False

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) > 12:
            return []
        
        self.ips = []
        def backtrace(s, start, path):
            if len(path) == 4 and start == len(s):
                self.ips.append(".".join(path))
            
            for i in range(start, len(s)):
                if i - start >= 3:  # 剪枝
                    continue
                if self.isValid(s[start:i+1]):
                    path.append(s[start:i+1])
                    backtrace(s, i+1, path)
                    path.pop()
        backtrace(s, 0, [])
        return self.ips
        


if __name__ == '__main__':
    s = '25525511135'
    print(Solution().restoreIpAddresses(s))



                


# @lc code=end

