class Solution:
    digitsWords = "abcdefghijklmnopqrstuvwxyz"
    # @return a list of strings, [s1, s2]
    def letterCombinations(self, digits):
        arr = ['']

        for digit in digits:
            words = self.getStringByNum(int(digit))
            arr = self.combineArray(arr, words)

        return arr

    def getStringByNum(self, num):
        if num < 2 or num > 10:
            return ['']
        
        ss = self.digitsWords[(num-2)*3:(num-1)*3]
        
        if num < 7:
            return ss
        elif num == 7:
            return "pqrs"
        elif num == 8:
            return "tuv"
        else:
            return "wxyz"

    def combineArray(self, arr1, arr2):
        arr = []
        for e1 in arr1:
            for e2 in arr2:
                arr.append(e1+e2)
        return arr

su = Solution()

print su.letterCombinations('200000235')