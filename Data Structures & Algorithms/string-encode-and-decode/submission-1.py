class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''

        for s in strs:
            res += str(len(s)) + '#' + s
        
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        n = len(s)
        res = []

        while i < n:
            num = ''

            while i < n and s[i].isnumeric():
                num += s[i]
                i += 1
            
            i += 1
            word = ''

            print(num)
            num = int(num)
            while num > 0:
                word += s[i]
                i += 1
                num -= 1
            
            # i += 1
            res.append(word)
        
        return res