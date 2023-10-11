class Solution:
    def select(self, arr, i):
        return arr[i]

    def selectionSort(self, arr, n):
        for i in range(len(arr)):
            min_indx = i
            for j in range(i + 1, len(arr)):
                if arr[min_indx] > arr[j]:
                    min_indx = j
            arr[i], arr[min_indx] = arr[min_indx], arr[i]
