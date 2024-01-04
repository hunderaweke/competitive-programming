class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        _sum = skill[0] + skill[-1]
        ans = skill[0] * skill[-1]
        n = len(skill)
        left,right  = 1 , n-2
        while left<right:
            if skill[left] + skill[right] != _sum:
                return -1
            ans += (skill[left] * skill[right])
            right -= 1
            left += 1
        return ans