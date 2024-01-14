class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(sublist,k):
          for i in range(k//2):
            sublist[i],sublist[k-i-1] = sublist[k-i-1],sublist[i]
        
        ans  = []
        valToSort = len(arr)

        while valToSort > 0:
          idx = arr.index(valToSort)
          if idx != valToSort -1:
            if idx != 0:
              ans.append(idx+1)
              flip(arr,idx+1)
            flip(arr,valToSort)
            ans.append(valToSort)
          valToSort -= 1
        return ans
            