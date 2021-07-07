#
# @lc app=leetcode.cn id=134 lang=python
#
# [134] 加油站
#

# @lc code=start
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        cur = 0
        total = 0
        start = 0
        for i in range(len(gas)):
            cur += gas[i] - cost[i]
            total += gas[i] - cost[i]
            if cur < 0:
                start = i+1
                cur = 0
            
        if total < 0:
            return -1

        return start


    def canCompleteCircuit0(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        暴力解法
        """
        n = len(gas)
        for i in range(n):
            start = (i+1) % n
            count = gas[i] - cost[i]
            while start != i:
                if count < 0:
                    break
                count += gas[start] - cost[start]
                start = (start + 1) % n 

            if count >= 0:
                return i
        return -1


if __name__ == '__main__':
    gas = [1,2,5,4,5]
    cost = [3,4,1,1,2]
    print(Solution().canCompleteCircuit(gas, cost))
                    
# @lc code=end

