class Solution:
    def minimumSteps(self, s: str) -> int:
        placeholder = 0
        s = list(s)
        while placeholder < len(s) and s[placeholder] != '1':
            placeholder += 1
        steps = 0
        for seeker in range(1,len(s)):
            if placeholder<len(s) and s[placeholder] == '1' and s[seeker] == '0' and seeker > placeholder:
                s[placeholder],s[seeker] = s[seeker],s[placeholder]
                steps += seeker-placeholder
                while placeholder < len(s) and s[placeholder] != '1':
                    placeholder += 1
        print("".join(s))
        return steps
    
 