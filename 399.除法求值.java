import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import java.util.Stack;

/*
 * @lc app=leetcode.cn id=399 lang=java
 *
 * [399] 除法求值
 */

// @lc code=start
class Solution {
    // public static void main(String[] args) {
    //     List<List<String>> equations = new ArrayList<List<String>>();
    //     equations.add(Arrays.asList("a", "b"));
    //     equations.add(Arrays.asList("b", "c"));
    //     double[] values = new double[]{2.0, 3.0};
    //     List<List<String>> queries = new ArrayList<List<String>>();
    //     queries.add(Arrays.asList("a", "c"));
    //     queries.add(Arrays.asList("b", "a"));
    //     queries.add(Arrays.asList("a", "e"));
    //     queries.add(Arrays.asList("a", "a"));
    //     queries.add(Arrays.asList("x", "x"));
    //     double[] res = new CalcEquation().calcEquation(equations, values, queries);
    //     for( int i=0; i < res.length; i++) {
    //         System.out.println(res[i]);
    //     }
    // }
    HashMap<String, HashMap<String, Double>> graph = new HashMap<String, HashMap<String, Double>>();
    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        int n = queries.size();
        int m = equations.size();
        double[] result = new double[n];
        // 初始化带权有向图
        for (int i = 0; i < m; i++) {
            List<String> equation = equations.get(i);
            String x = equation.get(0), y = equation.get(1);
            HashMap<String, Double> xy = graph.getOrDefault(x, new HashMap<String, Double>());
            HashMap<String, Double> yx = graph.getOrDefault(y, new HashMap<String, Double>());
            xy.put(y, values[i]);
            yx.put(x, 1.0 / values[i]);
            graph.put(x, xy);
            graph.put(y, yx);
        }
        for (int i = 0; i < n; i++) {
            List<String> query = queries.get(i);
            String src = query.get(0), dst = query.get(1);
            result[i] = BFS(src, dst);
            System.out.println(result[i]);
        }
        return result;
        
    }

    public double BFS(String src, String dst) {
        if (!graph.containsKey(src) || !graph.containsKey(dst)) {
            return -1.0;
        }
        String x = src;
        Double v = 1.0;
        Set<String> seen = new HashSet<String>();
        List<String> queue = new ArrayList<String>();
        List<Double> vv = new ArrayList<Double>();
        queue.add(x);
        vv.add(v);
        
        for (int i = 0; i < queue.size(); i++) {
            x = queue.get(i);
            v = vv.get(i);
            if (x.equals(dst)) {
                return v;
            }
            seen.add(x);
            for (String y: graph.get(x).keySet()){
                if (!seen.contains(y)) {
                    queue.add(y);
                    vv.add(v*graph.get(x).get(y));
                }
            }
        }
        return -1.0;
    }
}
// @lc code=end

