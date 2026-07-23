from functools import lru_cache

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        @lru_cache(None)
        def dp(pos):
            if pos >= n:
                return 1
            
            if 0 < int(s[pos]):
                one_way = dp(pos + 1)

                if pos + 1 < n and 0 < int(s[pos:pos+2]) < 27:
                    two_way = dp(pos + 2)
            
                else:
                    two_way = 0
            
            else:
                one_way = 0
                two_way = 0
            
            
            return one_way + two_way
        
        return dp(0)