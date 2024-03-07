class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        counter = {5:0,10:0}

        for bill in bills:
            if bill == 5:
                counter[5] += 1
            elif bill == 10:
                counter[10] += 1
                counter[5]-=1
            elif counter[10] > 0:
                counter[10] -= 1
                counter[5] -= 1
            else:
                counter[5] -= 3
            if counter[5] < 0:
                return False
        return True
