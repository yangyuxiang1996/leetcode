/*
 * @lc app=leetcode.cn id=77 lang=java
 *
 * [77] 组合
 */

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;

// @lc code=start
class Combine {
    List<List<Integer>> result = new ArrayList<>();
    LinkedList<Integer> path = new LinkedList<>();
    public List<List<Integer>> combine(int n, int k) {
        combineHelper(n, k, 1, path);
        return result;
    }

    /**
     * 每次从集合中选取元素，可选择的范围随着选择的进行而收缩，调整可选择的范围，就是要靠startIndex
     * @param startIndex 用来记录本层递归的中，集合从哪里开始遍历（集合就是[1,...,n] ）。
     */
    private void combineHelper(int n, int k, int startIndex, LinkedList<Integer> path){
        //终止条件
        if (k==path.size()){
            result.add(new ArrayList<>(path));
            return;
        }
        for (int i = startIndex; i <= n-(k-path.size())+1; i++){
            path.addLast(i);
            combineHelper(n, k, i + 1, path);
            path.removeLast();
        }
    }

    public static void main(String[] args) {
        int n = 4;
        int k = 4;
        System.out.println(new Combine().combine(n,k));
    }
}

// @lc code=end

