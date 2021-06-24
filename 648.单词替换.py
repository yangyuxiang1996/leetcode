#
# @lc app=leetcode.cn id=648 lang=python
#
# [648] 单词替换
#

# @lc code=start
class Solution(object):
    def replaceWords0(self, dictionary, sentence):
        """
        :type dictionary: List[str]
        :type sentence: str
        :rtype: str
        """
        sentence = sentence.split(' ')
        for i in range(len(sentence)):
            word = sentence[i]
            min_len = float("inf")
            for root in dictionary:
                if word.startswith(root):
                    if len(root) < min_len:
                        min_len = len(root)
                        sentence[i] = root
        
        return " ".join(sentence)



# @lc code=end

