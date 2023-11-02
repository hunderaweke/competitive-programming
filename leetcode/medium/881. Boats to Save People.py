class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right = len(people) - 1
        pairs = 0
        while left < right:
            tot = people[right] + people[left]
            if tot>limit:
                right -= 1
            if tot <= limit:
                right -= 1
                left +=1
                pairs += 1
        return len(people) - pairs
