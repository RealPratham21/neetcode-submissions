class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grps = defaultdict(list)

        for s in strs:
            sorted_s = ''.join(sorted(list(s)))

            grps[sorted_s].append(s)

        res = []

        for k, v in grps.items():
            res.append(v)
        
        return res