class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        re = self.reverseInt(x)
        return x == re
    
    def reverseInt(self, x):
        re = 0
        while x > 0:
            re = re * 10 + (x % 10)
            x = x / 10
        return re