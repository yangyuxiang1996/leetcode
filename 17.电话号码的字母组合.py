#
# @lc app=leetcode.cn id=17 lang=python
#
# [17] 电话号码的字母组合
#

# @lc code=start
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "" or digits == "1":
            return []
        num2letter = {
            1:"",
            2:"abc",
            3:"def",
            4:"ghi",
            5:"jkl",
            6:"mno",
            7:"pqrs",
            8:"tuv",
            9:"wxyz"
        }
        self.res = []
        def backtrace(start_i, path):
            if len(path) == len(digits):
                self.res.append(path)
                return
            
            # for i in range(start_i, len(digits)):
            letters = list(num2letter[int(digits[start_i])])
            for j in range(0, len(letters)):
                path += letters[j]
                backtrace(start_i+1, path)
                path = path[:-1]

        backtrace(0, "")
        return self.res


if __name__ == '__main__':
    digits = "23"
    print(Solution().letterCombinations(digits))



        
# @lc code=end

