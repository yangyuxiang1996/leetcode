class Solution(object):
    def replaceBlank(self, s):
        s = list(s)
        n = len(s)
        count = 0
        for i in range(n):
            if s[i] == ' ':
               count += 1

        s = s + [' '] * count * 2
        m = len(s)

        i, j = n-1, m-1
        while i != j:
            if s[i] != ' ':
                s[j] = s[i]
            else:
                s[j-2], s[j-1], s[j] = '%', '2', '0'
                j -= 2
            i -= 1
            j -= 1

        return "".join(s)


if __name__ == '__main__':
    s = "We are happy."
    print(Solution().replaceBlank(s))

        
