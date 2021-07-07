#
# @lc app=leetcode.cn id=406 lang=python
#
# [406] 根据身高重建队列
#

# @lc code=start
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        # 先按照身高从高到低排序
        people = sorted(people, key=lambda x: (-x[0], x[1]))
        new_people = []
        for person in people:
            new_people.insert(person[1], person)
        return new_people



if __name__ == '__main__':
    people = [[9,0],[7,0],[1,9],[3,0],[2,7],[5,3],[6,0],[3,4],[6,2],[5,2]]
    print(Solution().reconstructQueue(people))
# @lc code=end

