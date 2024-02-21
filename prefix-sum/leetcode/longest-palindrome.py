class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 1:
            return 1
        counter = Counter(s)
        odds = [cnt for _,cnt in counter.items() if cnt%2]
        evens = [cnt for _,cnt in counter.items() if not cnt%2]
        odds.sort()
        ans  = sum(evens)
        if not odds:
            return sum(evens) 
        for i in range(len(odds)-1):
            ans += odds[i]-1
        ans += odds[len(odds)-1]
        return ans        