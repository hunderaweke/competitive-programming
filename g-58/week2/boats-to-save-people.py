class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        count = 0
        left,right =0,len(people)-1
        while right >= left:
            _sum = people[right] + people[left]
            if _sum <= limit:
                left += 1
            count+= 1
            right -= 1
        return count 