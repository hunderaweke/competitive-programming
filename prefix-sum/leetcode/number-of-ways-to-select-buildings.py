class Solution:
    def numberOfWays(self, s: str) -> int:
        # since you can only form the 101 and 010 and the order matters
        # you can only form 101 if the current character is 0 there are prefix 1 and suffix ones
        # the number of the 101 substring you can get is the multiple of the number of prefix and suffix of 1 that you have
        # the same is for the 010 you can repeat the process
        """Using the tradtional prefix sum"""
        # zeros = [int('0' == ch) for ch in s]
        # ones = [int('1' == ch) for ch in s]
        # for i in range(1,len(s)):
        #     zeros[i] += zeros[i-1]
        #     ones[i] += ones[i-1]
        # res = 0
        # for i,ch in enumerate(s):
        #     if ch  == '0':
        #         res += ones[i] * (ones[-1]-ones[i])
        #     else:
        #         res += zeros[i] * (zeros[-1]-zeros[i])
        """Using simplified prefix sum"""
        zeros = s.count('0')
        ones = len(s) - zeros
        onesPrefix = zerosPrefix = res = 0
        for ch in s:
            if ch == '0':
                res += onesPrefix * (ones-onesPrefix)
                zerosPrefix += 1
            else:
                res += zerosPrefix * (zeros-zerosPrefix)
                onesPrefix  += 1
        return res
