class Solution:
    # @param s, a string
    # @return a string
    def reverseWords(self, s):
        arr = s.split()
        i = 0
        while i < len(arr)/2:
            tmp = arr[i];
            arr[i] = (arr[len(arr) - i - 1]).strip()
            arr[len(arr) - i - 1] = tmp.strip()
            i += 1
        r = " ".join(arr)
        return r