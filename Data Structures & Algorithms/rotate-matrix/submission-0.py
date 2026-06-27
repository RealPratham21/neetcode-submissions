import copy

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        new_mat = copy.deepcopy(matrix)
        n = len(matrix)

        col = n - 1

        for row in matrix:
            pos = 0
            
            for _ in range(n):
                new_mat[pos][col] = row[pos]

                # print(row[pos])
            
                pos += 1
            
            col -= 1
        
        # print(new_mat)
        # matrix = new_mat

        for i in range(n):
            for j in range(n):
                matrix[i][j] = new_mat[i][j]