class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        i = 0
        result = 0
        while i < len(A):
            result ^= A[i]
            i += 1
        return result