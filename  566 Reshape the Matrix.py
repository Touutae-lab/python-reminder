class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        result = list()
        if (m * n != r * c):
            return mat
        
        value = [value for i in mat for value in i]
        count = 0
        for i in range(r):
            result.append([])
            for j in range(c):
                result[i].append(value[count])
                count += 1
        return result