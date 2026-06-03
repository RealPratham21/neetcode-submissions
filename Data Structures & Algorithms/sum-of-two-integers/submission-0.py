class Solution:
    def getSum(self, a: int, b: int) -> int:
        res = ''
        carry = 0

        for i in range(32):
            if carry > 0:
                res = '1' + res
                carry -= 1
            
            else:
                a_bit = a & (1 << i)
                b_bit = b & (1 << i)

                if a_bit and b_bit:
                    res = '0' + res
                    carry += 1
                
                elif (a_bit > 0 and b_bit == 0) or (a_bit == 0 and b_bit > 0):
                    res = '1' + res
                
                else:
                    res = '0' + res
        
        return int(res, 2)