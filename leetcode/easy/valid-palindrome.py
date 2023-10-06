from string import ascii_letters,digits
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s.replace(' ','')
        s = ''.join((filter(lambda i:i in ascii_letters or i  in digits,s)))
        s = s.lower()
        if s[::-1] == s:
            return True
        return False