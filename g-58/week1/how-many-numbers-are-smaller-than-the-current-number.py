from collections import Counter
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = sorted(nums)
        dic = dict()
        for i in nums:
            if i not in dic:
                dic[i] = n.index(i)
            else:
                continue
        res = [dic[i] for i in nums]
        return res