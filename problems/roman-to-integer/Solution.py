class Solution:
    myDict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    # @return an integer
    def romanToInt(self, s):
        result = self.myDict[s[len(s) - 1]]

        i = len(s)

        while i > 1:
            if self.myDict[s[i-1]] > self.myDict[s[i-2]]:
                result -= self.myDict[s[i-2]]
            else:
                result += self.myDict[s[i-2]]

            i -= 1

        return result

su = Solution()

print su.romanToInt('XIV')

# No need to worry about 'IIX', because 'VIII' represent 8