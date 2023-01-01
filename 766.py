class Solution:
    def isToeplitzMatrix(self, matrix: list[list[int]]) -> bool:
        m = matrix.__len__()
        n = matrix[0].__len__()
        k = min(m,n)
        for di in range(m):
            checkValue = matrix[di][0]
            for i in range(1,min(m-di,k)):
                if checkValue != matrix[di+i][i]:
                    return False
        for dj in range(1,n):
            checkValue = matrix[0][dj]
            for j in range(1,min(n-dj,k)):
                if checkValue != matrix[j][dj+j]:
                    return False
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.isToeplitzMatrix([[1,2,3,4],[5,1,2,3],[9,5,1,2]]))
    print(s.isToeplitzMatrix([[1,2],[2,2]]))