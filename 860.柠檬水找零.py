#
# @lc app=leetcode.cn id=860 lang=python
#
# [860] 柠檬水找零
#

# @lc code=start
class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        if bills[0] != 5:
            return False
        
        m = {5:0, 10:0, 20:0}
        for bill in bills:
            if bill == 5:
                m[bill] += 1
            elif bill == 10:
                if m[5] == 0:
                    return False
                else:
                    m[5] -= 1
                m[10] += 1
            elif bill == 20:
                if m[10] > 0 and m[5] > 0:
                    m[10] -= 1
                    m[5] -= 1
                elif m[10] == 0 and m[5] > 3:
                    m[5] -= 3
                else:
                    return False
                m[20] += 1
                    
        return True

        

# @lc code=end

