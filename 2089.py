class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        orderedNum, targetCnt = 0, 0
        for i in nums:
            if i < target:
                orderedNum += 1
            elif i == target:
                targetCnt += 1
        return [i for i in range(orderedNum, orderedNum+targetCnt)]
        

s = Solution()
print(s.targetIndices(nums = [1,2,5,2,3], target = 2))
print(s.targetIndices(nums = [1,2,5,2,3], target = 3))
print(s.targetIndices(nums = [1,2,5,2,3], target = 5))