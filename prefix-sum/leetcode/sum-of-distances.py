class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0]*n
        index_map = defaultdict(int)
        frequency = defaultdict(int)
        for i,num in enumerate(nums):
            if num in index_map:
                prefix[i] += (i*frequency[num]) - index_map[num]
            frequency[num] += 1
            index_map[num] += i
        index_map.clear()
        frequency.clear()
        for i in range(n-1,-1,-1):
            if nums[i] in index_map:
                prefix[i] +=  index_map[nums[i]]- (i*frequency[nums[i]])
            frequency[nums[i]] += 1
            index_map[nums[i]] += i
        return prefix