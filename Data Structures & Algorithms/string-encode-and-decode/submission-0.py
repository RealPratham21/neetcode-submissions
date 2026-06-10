class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''

        for i in strs:
            if not res:
                res += i
            
            else:
                res += 'vh66'
                res += i
        
        return res


    def decode(self, s: str) -> List[str]:
        res = s.split('vh66')

        return res