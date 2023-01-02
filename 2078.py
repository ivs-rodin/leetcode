class Solution:
    def maxDistance(self, colors: list[int]) -> int:
        n = colors.__len__()
        i = 0
        j = n-1
        while colors[0] == colors[j] and j>0:
            j -= 1
        while colors[n-1] == colors[i] and i<n-1:
            i += 1
        return max(n-1-i, j)

s = Solution()
print(s.maxDistance([1,1,1,1,1,1,1]))
print(s.maxDistance([1,8,3,8,3]))
print(s.maxDistance([0,1]))