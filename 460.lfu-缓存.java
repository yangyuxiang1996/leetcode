/*
 * @Description: 
 * @Author: yangyuxiang
 * @Date: 2021-05-06 10:33:41
 * @LastEditors: yangyuxiang
 * @LastEditTime: 2021-05-06 11:42:44
 * @FilePath: /leetcode/460.lfu-缓存.java
 */
/*
 * @lc app=leetcode.cn id=460 lang=java
 *
 * [460] LFU 缓存
 */

// @lc code=start

import java.util.*;

class LFUCache {
    HashMap<Integer, Integer> keyToVal;
    HashMap<Integer, Integer> keyToFreq;
    HashMap<Integer, LinkedHashSet<Integer>> freqToKey;
    int minFreq;
    int capacity;

    public LFUCache(int capacity) {
        this.keyToVal = new HashMap<Integer, Integer>();
        this.keyToFreq = new HashMap<Integer, Integer>();
        this.freqToKey = new HashMap<Integer, LinkedHashSet<Integer>>();
        this.minFreq = 0;
        this.capacity = capacity; 
    }

    public void increaseFreq(int key) {
        int freq = this.keyToFreq.get(key);
        this.keyToFreq.put(key, freq + 1);
        
        this.freqToKey.get(freq).remove(key);
        this.freqToKey.putIfAbsent(freq+1, new LinkedHashSet<Integer>());
        this.freqToKey.get(freq+1).add(key);

        if (this.freqToKey.get(freq).isEmpty()) {
            this.freqToKey.remove(freq);
            if (freq == this.minFreq){
                this.minFreq++;
            }
        }
    }

    public void removeLeastFreq() {
        LinkedHashSet<Integer> keyList = this.freqToKey.get(this.minFreq);
        int deletedKey = keyList.iterator().next();
        this.keyToVal.remove(deletedKey);
        this.keyToFreq.remove(deletedKey);
        this.freqToKey.get(this.minFreq).remove(deletedKey);
        if (this.freqToKey.get(this.minFreq).isEmpty()) {
            this.freqToKey.remove(this.minFreq);
        }

    }
    
    public int get(int key) {
        if (!this.keyToVal.containsKey(key)) {
            return -1;
        }
        increaseFreq(key);
        return this.keyToVal.get(key);
        
    }
    
    public void put(int key, int value) {
        if (this.capacity <= 0) return;

        if (this.keyToVal.containsKey(key)){
            this.keyToVal.put(key, value);
            increaseFreq(key);
            return;
        }
        
        if (this.capacity <= this.keyToVal.size()){
            removeLeastFreq();
        } 
        this.keyToVal.put(key, value);
        this.keyToFreq.put(key, 1);
        this.freqToKey.putIfAbsent(1, new LinkedHashSet<Integer>());
        this.freqToKey.get(1).add(key);
        this.minFreq = 1;
        
        return;
    }
}

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache obj = new LFUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
// @lc code=end

