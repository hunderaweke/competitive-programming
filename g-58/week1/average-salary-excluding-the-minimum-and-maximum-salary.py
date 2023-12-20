class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        _sum = sum(salary[1:len(salary)-1])
        return _sum/(len(salary)-2)