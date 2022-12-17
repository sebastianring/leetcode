class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        #DO A BINARY SEARCH DUDE
        l = 0
        r = len(nums)-1

        while l < r:
            m = (l + r) // 2
            if target == nums[m]:
                return m
            elif target > nums[m]:
                l = m + 1
            else:
                r = m
        
        if target > nums[l]:
            return r+1
        elif r < 0:
            return 0

        return r


p = Solution()
print(p.searchInsert(nums = [1,3,5,6,7,8,9,10], target = 5)) # 2
print(p.searchInsert(nums = [1,3,5,6], target = 2)) # 1
print(p.searchInsert(nums = [1,3,5,6], target = 7)) # 4
print(p.searchInsert(nums = [1,3,5,6], target = 0)) # 0
print(p.searchInsert(nums = [2,3,4,8,10], target = 0)) # 0
