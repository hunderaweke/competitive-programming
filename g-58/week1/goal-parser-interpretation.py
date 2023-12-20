class Solution:
    def interpret(self, command: str) -> str:
        res = ""
        left = 0
        for right in range(len(command)):
            if command[right] == '(':
                left = right
            elif command[right] == ')':
                if right - left == 1:
                    res += 'o'
                else:
                    res += "al"
            elif command[right] == "G":
                res += "G"
        return res
