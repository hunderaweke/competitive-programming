class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ptr1,ptr2 = 0,0 
        intersections = []
        while ptr1 < len(firstList) and ptr2 < len(secondList):
          first_start,first_end = firstList[ptr1]
          second_start,second_end = secondList[ptr2]
          if second_start <= first_end and first_start <= second_end:
            start = max(first_start,second_start)
            end = min(first_end,second_end)
            intersections.append([start,end])
          if ptr2 == len(secondList)-1 or first_end < second_end:
            ptr1 += 1
          else:
            ptr2 += 1
        return intersections

        