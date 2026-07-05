class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        stack = []

        for s, e in intervals:
            if stack and (s <= stack[-1][-1] <= e or stack[-1][0] <= s <= stack[-1][-1]):
                stack[-1] = [min(stack[-1][0], s), max(stack[-1][1], e)]
            
            else:
                stack.append([s, e])
        
        return stack