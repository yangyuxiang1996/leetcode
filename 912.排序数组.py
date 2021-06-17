#
# @lc app=leetcode.cn id=912 lang=python
#
# [912] 排序数组
#

# @lc code=start
class Solution(object):
    def sortArray(self, nums):

        def merge_sort(nums, l, r):
            """
            :type nums: List[int]
            :rtype: List[int]
            归并排序, inplace
            """
            if l >= r:
                return

            mid = l + (r - l) // 2
            merge_sort(nums, l, mid)
            merge_sort(nums, mid+1, r)
            tmp = []
            # 利用两个指针分别遍历左右两个数组
            i, j = l, mid+1
            while i <= mid and j <= r:
                if nums[j] < nums[i]:
                    tmp.append(nums[j])
                    j += 1
                else:
                    tmp.append(nums[i])
                    i += 1
            while j <= r:
                tmp.append(nums[j])
                j += 1
            while i <= mid:
                tmp.append(nums[i])
                i += 1

            nums[l:r+1] = tmp

        merge_sort(nums, 0, len(nums)-1)
        return nums


if __name__ == '__main__':
    nums = [5,2,3,1]
    print(Solution().sortArray(nums))





        
# @lc code=end

