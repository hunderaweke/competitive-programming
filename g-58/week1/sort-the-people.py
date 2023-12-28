class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people = list(zip(heights,names))
        people.sort(reverse=True)
        ans  = [person[1] for person in people]
        return ans