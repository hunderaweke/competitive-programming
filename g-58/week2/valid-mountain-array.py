class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        # Find the Maximum number for contructing the mountain
        max_num = max(arr)
        # Find the index of the initial occurence of the mountain
        max_index = arr.index(max_num)
        if max_index == 0 or max_index == len(arr)-1:
            return False
        # Checking for the left side of the arr if it is mountain
        for i in range(max_index):
            if arr[i] == max_num or arr[i] >= arr[i+1]:
                return False
        # checking for the right side of the arr if it is mountain
        for i in range(len(arr)-1,max_index,-1):
            if arr[i] == max_num or arr[i] >= arr[i-1]:
                return False
        return True