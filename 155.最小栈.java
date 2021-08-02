import java.util.Deque;
import java.util.LinkedList;

/*
 * @lc app=leetcode.cn id=155 lang=java
 *
 * [155] 最小栈
 */

// @lc code=start
class MinStack {
    Deque<Integer> xStack;
    Deque<Integer> minStack;

    /** initialize your data structure here. */
    public MinStack() {
        xStack = new LinkedList<Integer>();
        minStack = new LinkedList<Integer>();
        minStack.push(Integer.MAX_VALUE);
    }
    
    public void push(int val) {
        // 将元素 x 推入栈中
        xStack.push(val);
        minStack.push(Math.min(val, minStack.peek()));
    }
    
    public void pop() {
        // 删除栈顶的元素
        xStack.pop();
        minStack.pop();
    }
    
    public int top() {
        // 获取栈顶元素
        return xStack.peek(); 
    }
    
    public int getMin() {
        // 检索栈中的最小元素
        return minStack.peek();
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */
// @lc code=end

