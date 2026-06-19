class Solution:
    def hammingWeight(self, n: int) -> int:
        res = 0

        curr = 1

        for _ in range(32):

            if n & curr:
                res += 1
            
            curr <<= 1
        
        return res