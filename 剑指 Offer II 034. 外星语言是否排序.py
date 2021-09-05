#!/usr/bin/env python
# coding=utf-8
'''
Author: Yuxiang Yang
Date: 2021-09-03 08:35:00
LastEditors: Yuxiang Yang
LastEditTime: 2021-09-03 12:52:11
FilePath: /leetcode/剑指 Offer II 034. 外星语言是否排序.py
Description: 
某种外星语也使用英文小写字母，但可能顺序 order 不同。字母表的顺序（order）是一些小写字母的排列。
给定一组用外星语书写的单词 words，以及其字母表的顺序 order，只有当给定的单词在这种外星语中按字典序排列时，返回 true；否则，返回 false。
输入：words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
输出：true
解释：在该语言的字母表中，'h' 位于 'l' 之前，所以单词序列是按字典序排列的。
'''
class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        
        m = {}
        for c in order:
            m[c] = len(m)
        
        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            l1, l2 = len(w1), len(w2)

            for i in range(max(l1, l2)):
                if i >= l1:
                    i1 = -1
                else:
                    i1 = m[w1[i]]
                
                if i >= l2:
                    i2 = -1
                else:
                    i2 = m[w2[i]]
                
                if i1 > i2:
                    return False
                elif i1 == i2:
                    continue
                else:
                    break
        return True


if __name__ == '__main__':
    words = ["word","world","row"]
    order = "worldabcefghijkmnpqstuvxyz"
    print(Solution().isAlienSorted(words, order))


