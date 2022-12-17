class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        #DO A BINARY SEARCH DUDE
        prev = -10000
        for i in range(len(nums)):
            if target >= prev and target <= nums[i]:
                return i
            else:
                prev = nums[i]
        
        return i+1


p = Solution()
print(p.searchInsert(nums = [1,3,5,6], target = 5))
print(p.searchInsert(nums = [1,3,5,6], target = 2))
print(p.searchInsert(nums = [1,3,5,6], target = 7))
print(p.searchInsert(nums = [1,3,5,6], target = 0))
print(p.searchInsert(nums = [2,3,4,8,10], target = 0))
