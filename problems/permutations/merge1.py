class Merge(object):
    arr = []
    temp = []
    def mergeSort(self, arr):
        self.arr = arr
        self.temp = [None] * len(arr)
        self.doMerge(0, len(arr) - 1)

        return self.arr

    def doMerge(self, first, last):
        if first < last:
            mid = (first + last) / 2
            self.doMerge(first, mid)
            self.doMerge(mid + 1, last)
            self.merge(first, mid, last)

    def merge(self, first, mid, last):
        i = first
        j = mid + 1
        k = 0

        while i <= mid and j <= last:
            if self.arr[i] < self.arr[j]:
                self.temp[k] = self.arr[i]
                k += 1
                i += 1
            else:
                self.temp[k] = self.arr[j]
                k += 1
                j += 1

        while i <= mid:
            self.temp[k] = self.arr[i]
            k += 1
            i += 1
        
        while j <= last:
            self.temp[k] = self.arr[j]
            k += 1
            j += 1
        
        i = 0
        while i < k:
            self.arr[first+i] = self.temp[i]
            i += 1


me = Merge()

# print me.merge([2], [1])

print me.mergeSort([3,1,1,-3,4,2])