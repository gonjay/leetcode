class Solution:
# @param num, a list of integer
# @return a list of lists of integers
    def permute(self, num):
        return self._permute(num)


    def _permute(self, num):
        if len(num) == 1:
            return [num]
        if len(num) == 2:
            return [[num[0], num[1]], [num[1], num[0]]]  
        ret = []
        for i in xrange(len(num)):
            # print i,num
            # print num[:i] + num[i+1:]
            _ret = self._permute(num[:i] + num[i+1:])
            print '      _ret:',_ret
            print 'origin ret:',ret
            print '    num[i]:',num[i],'i',i
            print '    extend:',[[num[i]] + one for one in _ret]
            ret.extend([[num[i]] + one for one in _ret])
            print 'ret.extend:',ret,'\n'
        return ret


su = Solution()

print su.permute([1,2,3])

# print su.outputs

# su.perm([1,2,3])

# print su.outputs