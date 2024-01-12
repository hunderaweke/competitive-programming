class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        pre = [0]*len(flips)
        pre[0] = flips[0]
        for i in range(1,len(flips)):
            pre[i] += pre[i-1]+flips[i]
        indexPreSum = [0]*len(flips)
        indexPreSum[0]=1
        for i in range(1,len(flips)):
          indexPreSum[i] += indexPreSum[i-1]+i+1
        count = 0 
        for idx in range(len(flips)):
          count +=  indexPreSum[idx] == pre[idx]
        return count