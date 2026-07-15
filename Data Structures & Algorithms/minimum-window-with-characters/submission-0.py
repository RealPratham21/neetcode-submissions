from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        curr_window = {}

        for c in s + t:
            curr_window[c] = 0

        expected = Counter(t)

        l = 0
        n = len(s)
        res = ''
        min_len_so_far = float('inf')

        for r in range(n):
            curr_window[s[r]] += 1

            all_present = True

            for c in expected.keys():
                if curr_window[c] < expected[c]:
                    all_present = False
                    break
            
            if all_present:
                while l < r and curr_window[s[l]] > expected[s[l]]:
                    curr_window[s[l]] -= 1
                    l += 1
            
                curr_len = r - l + 1

                if curr_len < min_len_so_far:
                    min_len_so_far = curr_len
                    res = s[l:r+1]
        
        return res