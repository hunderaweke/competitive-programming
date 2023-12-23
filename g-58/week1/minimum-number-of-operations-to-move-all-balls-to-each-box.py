class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        counter = defaultdict(list)
        for i in range(len(boxes)):
            for j in range(len(boxes)):
                if boxes[j]=='1':
                    counter[i].append(abs(j-i))
        ans  = [0]*len(boxes)
        for indx in counter:
            ans[indx] = (sum(counter[indx])) 
        return ans