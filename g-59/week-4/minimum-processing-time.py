class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort(reverse=True)
        tasks.sort()
        max_time = 0
        pro = 0
        for i in range(3,len(tasks),4):
          max_time = max(max_time,processorTime[pro]+tasks[i])
          pro+=1
        return max_time