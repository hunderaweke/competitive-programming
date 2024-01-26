class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        carrier = [0]*1001
        for passengers,start,end in trips:
            carrier[start] += passengers
            carrier[end] -= passengers
        for i in range(1001):
            if i > 0:
                carrier[i] += carrier[i-1]
            if carrier[i] > capacity:
                return False
        return True