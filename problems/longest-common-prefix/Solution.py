class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if len(strs) < 1: return ""
        length = len(strs[0])
        for str in strs[1:]:
            length = min(length, len(str))
            for i in range(length):
                if str[i] != strs[0][i]:
                    length = i
                    break
                
        return strs[0][:length]