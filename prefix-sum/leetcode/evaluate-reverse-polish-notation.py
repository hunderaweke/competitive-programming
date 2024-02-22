class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack  = []
        symbols = {'+','-','/','*'}
        for token in tokens:
            if token in symbols:
                first_operand = stack.pop()
                second_operand = stack.pop()
                res = eval(f"{second_operand}{token}{first_operand}")                                        
                result = floor(res) if res > 0 else ceil(res)
                stack.append(result)
            else:
                stack.append(token)
        return int(stack[-1])