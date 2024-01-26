class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        hash_map = defaultdict(int)
        hash_map[0]+=1
        prefix_sum = 0
        count = 0
        for i in range(len(nums)):
            prefix_sum+= nums[i]
            count += hash_map[prefix_sum%k]
            hash_map[prefix_sum%k] += 1
        return count