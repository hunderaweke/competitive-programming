class Solution:
    def smallestNumber(self, num: int) -> int:
        s = list(sorted(str(abs(num)),reverse = num < 0),)
        firstNonZero = next((i for i,c in enumerate(s) if c != '0'),0)
        s[0],s[firstNonZero] = s[firstNonZero],s[0]
        return int(''.join(s)) * (-1 if num<0 else 1)