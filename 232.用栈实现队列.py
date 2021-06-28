#
# @lc app=leetcode.cn id=232 lang=python
#
# [232] 用栈实现队列
#

# @lc code=start
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.listA = []
        self.listB = []
        self.size = 0


    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        self.listA.append(x)
        self.size += 1


    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        if self.listB == []:
            while self.listA:
                tmp = self.listA.pop()
                self.listB.append(tmp)
        self.size -= 1
        return self.listB.pop()


    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        # if self.listB == []:
        #     while self.listA:
        #         tmp = self.listA.pop()
        #         self.listB.append(tmp)
        # return self.listB[-1]
        tmp = self.pop()
        self.listB.append(tmp)
        self.size += 1
        return tmp


    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return self.size == 0



# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
print(obj.peek())
print(obj.pop())
print(obj.empty())

# @lc code=end

