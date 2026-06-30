class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0

        res = 0
        n = len(s)
        max_char = ''
        cmax = 0
        cnt = Counter(s)

        for key, v in cnt.items():
            if v > cmax:
                cmax = v
                max_char = key
        
        subs = 0

        for r in range(n):
            if s[r] != max_char:
                subs += 1
            
            while subs > k:
                if s[l] != max_char:
                    subs -= 1
                
                l += 1
            
            res = max(res, r - l + 1)
        
        return res