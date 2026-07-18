class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        l, r = 0, len(matrix[0]) - 1
        top, bottom = 0, len(matrix) - 1

        res = []

        while l <= r or top <= bottom:
            if top <= bottom:
                for i in range(l, r + 1):
                    res.append(matrix[top][i])
                
                top += 1

            if l <= r:
                for i in range(top, bottom + 1):
                    res.append(matrix[i][r])
                
                r -= 1

            if top <= bottom:
                for i in range(r, l - 1, -1):
                    res.append(matrix[bottom][i])
                
                bottom -= 1

            if l <= r:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][l])
                
                l += 1
        
        return res