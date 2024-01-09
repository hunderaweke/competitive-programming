class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):return False
        s1Counter,s2Counter = {},{}
        for i in range(len(s1)):
            s1Counter[s1[i]] = 1 + s1Counter.get(s1[i],0)
            s2Counter[s2[i]] = 1 + s2Counter.get(s2[i],0)
        if s1Counter == s2Counter:
            return True
        left = 0
        for right in range(len(s1),len(s2)):
            s2Counter[s2[right]] = 1 + s2Counter.get(s2[right],0)
            s2Counter[s2[left]] -= 1
            if s2Counter[s2[left]] ==0:
                s2Counter.pop(s2[left])
            if s1Counter == s2Counter:
                return True
            left += 1
        return False