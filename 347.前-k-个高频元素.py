#
# @lc app=leetcode.cn id=347 lang=python
#
# [347] 前 K 个高频元素
#

# @lc code=start
import heapq
class Solution(object):
    def topKFrequent0(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        
        count = sorted(count.items(),key = lambda x:x[1],reverse = True)
        return list(map(lambda x:x[0], count))[:k]
    
    
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        
        # 小顶堆
        pri_que = []
        for key, value in count.items():
            heapq.heappush(pri_que, (value, key))
            if len(pri_que) > k:
                heapq.heappop(pri_que)
        
        res = []
        while pri_que:
            res.append(pri_que.pop()[1])

        return res

# @lc code=end

