#
# @lc app=leetcode.cn id=225 lang=python3
#
# [225] 用队列实现栈
#

# @lc code=start
from collections import deque
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.deque1 = deque()
        self.deque2 = deque()


    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.deque1.append(x)


    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        这里只能利用deque的popleft方法，因此需要deque2存储
        """
        size = len(self.deque1)
        while size > 1:
            self.deque2.append(self.deque1.popleft())
            size -= 1
        tmp = self.deque1.popleft()
        self.deque1, self.deque2 = self.deque2, self.deque1
        return tmp
        

    def top(self) -> int:
        """
        Get the top element.
        """
        return self.deque1[-1]


    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.deque1) == 0



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
# @lc code=end

