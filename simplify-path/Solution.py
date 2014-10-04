class Solution:
    def simplifyPath(self, path):
        arr = path.split('/')

        print arr

        p_arr = []

        for p in arr:
            if p == '..':
                if p_arr:
                    p_arr.pop()
            elif p != '' and p != '.':
                p_arr.append(p)

        print p_arr

        return '/' + '/'.join(p_arr)

su = Solution()

print su.simplifyPath('/..')