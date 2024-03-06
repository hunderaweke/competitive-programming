class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # The most important thing we need to determinte is the variable that we need to make our search on 
        # For this case it is the weight that we need to transfer using the boat
        left,right,best = max(weights),sum(weights),-1

        while left<= right:

            mid = (left + right)//2
            # computing the number of days could take using the current best weight capacity

            computed_days = 1
            counter = 0
        
            for i in range(len(weights)):
                counter += weights[i]
                if counter > mid:
                    counter = weights[i]
                    computed_days += 1

            if computed_days  > days:
                left = mid + 1
            else:
                right = mid - 1
                best = mid 
         
        return best