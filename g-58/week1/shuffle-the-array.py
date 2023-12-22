class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []
        cnt = 1
        for i in range(2*n):
            if i %2 == 0 :
                res.append(nums[i//2])
            else:
                res.append(nums[n + i - cnt])
                cnt +=1
        return res