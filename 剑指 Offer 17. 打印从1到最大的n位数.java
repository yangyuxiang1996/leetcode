import java.util.Deque;
import java.util.LinkedList;

class Solution {
    public int[] printNumbers(int n) {
        int[] res = new int[(int)Math.pow(10, n)-1];
        Deque<String> stack = new LinkedList<String>();
        int index = 0;

        for (int i = 1; i <= 9; i++) {
            stack.add(String.valueOf(i));
        }

        while (!stack.isEmpty()) {
            int length = stack.size();
            for (int i = 0; i < length; i++) {
                String cur = stack.pop();
                res[index++] = Integer.parseInt(cur);
                if (cur.length() < n) {
                    for (int j = 0; j < 10; j++) {
                        String tmp = cur + String.valueOf(j);
                        stack.add(tmp);
                    }
                }
            }
        }
        return res;
    }
}

            
            
