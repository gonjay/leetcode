# Reverse digits of an integer.
#
# Example1: x = 123, return 321
# Example2: x = -123, return -321

class Solution:
    # @return an integer
    def reverse(self, x):
        reverseInt = 0
        flag = 1
        if x < 0:
            x = abs(x)
            flag = -1
        while x != 0:
            reverseInt = reverseInt * 10 + x % 10
            x = x / 10
        return reverseInt * flag


su = Solution()

print su.reverse(-123)