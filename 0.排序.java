import java.util.Arrays;

/*
 * @Author: Yuxiang Yang
 * @Date: 2021-08-10 20:06:15
 * @LastEditors: Yuxiang Yang
 * @LastEditTime: 2021-08-10 20:52:07
 * @FilePath: /leetcode/0.排序.java
 * @Description: 
 */

class MySort {
    public static void main(String[] args) {
        int[] nums1 = new int[] { 1, 3, 4, 6, 2, 1, 4, 5, 9, 7 };
        int[] nums2 = new int[] { 1, 3, 4, 6, 2, 1, 4, 5, 9, 7 };
        new MySort().quickSort(nums1, 0, nums1.length - 1);
        System.out.println(Arrays.toString(nums1));
        new MySort().quickSort(nums2, 0, nums2.length - 1);
        System.out.println(Arrays.toString(nums2));
    }

    public int partition(int[] nums, int left, int right) {
        int pivot = nums[left];
        int i = left, j = right;
        while (i < j) {
            while (i < j && nums[j] >= pivot) {
                j--;
            }
            if (i < j) {
                nums[i] = nums[j];
            }
            while (i < j && nums[i] <= pivot) {
                i++;
            }
            if (i < j) {
                nums[j] = nums[i];
            }
        }
        nums[i] = pivot;
        return i;
    }

    public void quickSort(int[] nums, int left, int right) {
        if (left >= right) {
            return;
        }
        int mid = partition(nums, left, right);
        quickSort(nums, left, mid - 1);
        quickSort(nums, mid + 1, right);
    }

    public void merge(int[] nums, int left, int mid, int right) {
        int[] tmp = new int[right - left + 1];
        int i = left, j = mid+1;
        int k = 0;
        while (i <= mid && j <= right) {
            if (nums[i] <= nums[j]) {
                tmp[k] = nums[i];
                i++;
            } else {
                tmp[k] = nums[j];
                j++;
            }
            k++;
        }
        while (i <= mid) {
            tmp[k] = nums[i];
            i++;
            k++;
        }
        while (j <= right) {
            tmp[k] = nums[j];
            j++;
            k++;
        }

        for (int t = 0; i <= tmp.length; i++) {
            nums[t+left] = tmp[t];
        }
    }
    
    public void mergeSort(int[] nums, int left, int right) {
        if (left >= right) {
            return;
        }
        int mid = left + (right - left) / 2;
        mergeSort(nums, left, mid);
        mergeSort(nums, mid+1, right);
        merge(nums, left, mid, right);
    }
}
