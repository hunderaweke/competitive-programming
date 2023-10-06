class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people) -1
        pairs = 0
        while l<r:
            s = people[l]+people[r]
            if s > limit:
                r-=1
            elif s <= limit:
                pairs +=1
                r -= 1
                l += 1
        return len(people) - (pairs)