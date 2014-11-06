class Solution:
    # @param A, a list of integers
    # @return an integer
    def trap(self, A):
        i = 0
        m = 0
        x = 0
        m_right = 0
        c_max = 0
        c_max_index = 0
        while i < len(A) - 1:
            if A[i+1] < A[i]:
                m = i + 1
                while m < len(A):
                    if A[m] < A[i]:
                        # record max
                        if A[m] > c_max:
                            c_max = A[m]
                            c_max_index = m
                        m += 1
                    else:
                        break
                if m < len(A):
                    m_right = m
                m -= 1
                if m+1 < len(A):
                    while m > i:
                        print "m",m,"A[m]",A[m]
                        print A[i],A[m],A[i] - A[m]
                        print '*'*10
                        x = x + (A[i] - A[m])
                        m -= 1
            if m_right > i:
                i = m_right
            else:
                i += 1
        
        print x

    def trap2(self, A):
        i = 0
        while i < len(A) - 1:
            j = i - 1
            max_left_j = i
            while j > 0:
                if A[j] > A[max_left_j]:
                    max_left_j = j
                j -= 1
            k = i + 1
            max_right_k = i
            while k < len(A):
                if A[k] > A[max_right_k]:
                    max_right_k = k
                k += 1
            if max_left_j != i and max_right_k != i:
                if max_left_j > max_right_k:
                    
        pass

su = Solution()

su.trap([0,1,0,2,1,0,1,3,2,1,2,1])