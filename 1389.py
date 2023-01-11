class Solution:
    def createTargetArray(self, nums: list[int], index: list[int]) -> list[int]:
        target = []
        for i,n in zip(index,nums): 
            target[i:i] = [n]
        return target

s = Solution()

print(s.createTargetArray(nums = [1,2,3,4,0], index = [0,1,2,3,0]))
print(s.createTargetArray(nums = [0,1,2,3,4], index = [0,1,2,2,1]))
print(s.createTargetArray(nums = [1], index = [0]))