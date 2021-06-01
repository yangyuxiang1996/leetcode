import java.util.Stack;

/*
 * @Description: 
 * @Author: yangyuxiang
 * @Date: 2021-05-17 23:29:09
 * @LastEditors: yangyuxiang
 * @LastEditTime: 2021-05-17 23:51:04
 * @FilePath: /leetcode/224.基本计算器.java
 */
/*
 * @lc app=leetcode.cn id=224 lang=java
 *
 * [224] 基本计算器
 */

// @lc code=start
class Solution {
    public int calculate(String s) {
        String S = s;
        return calcu(S);
    }
    //index全局变量,递归时方便使用
    int index = 0;
    public int calcu(String s){
        Stack<Integer> stack = new Stack<>();
        int sum = 0;
        char sign = '+';
        int num = 0;
        while(index < s.length()){
            char c = s.charAt(index++);
            //如果是数字转换为int型
            if(Character.isDigit(c)){
                num = num * 10 + (c - '0');
            }
            //遇到括号,就递归解决
            if(c == '('){
                num = calculate(s);
            }
            //如果不是,就把符号后边的数字处理后加入栈中
            if((!Character.isDigit(c) && c != ' ') || index == s.length()){
                int tmp;
                switch(sign){

                    case '+' : {
                        stack.push(num);
                    } 
                    break;
                    case '-' : {
                        stack.push(-num);
                    }
                    break;
                    case '*' : {
                        tmp = stack.pop() * num;
                        stack.push(tmp);
                    }
                    break;
                    case '/': {
                        tmp = stack.pop() / num;
                        stack.push(tmp);
                    }
                    break;
                }
                //重新归0,操作符设置为c;
                num = 0;
                sign = c;
            }
            //遇到右括号就停止计算
            if(c == ')'){
                break;
            }
    }
            sum = 0;
            //计算总数并返回
            while(!stack.isEmpty()){
                sum += stack.pop();
            }
            return sum;
    }                   
}

// @lc code=end

