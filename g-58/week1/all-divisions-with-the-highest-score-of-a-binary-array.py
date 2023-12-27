class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        # Count the number of ones
        counter ={0:0,1:Counter(nums)[1]}
        indices = defaultdict(list)
        # Appending the count of ones as a default 
        indices[counter[1]].append(0)
        indices[nums.count(0)].append(len(nums))
        for index in range(1,len(nums)):
            if nums[index-1] == 1:
                counter[1] -= 1
            elif nums[index-1] == 0:
                counter[0] += 1
            division_sum = counter[0] + counter[1]
            indices[division_sum].append(index)
        max_sum = max(indices.keys())
        return indices[max_sum]