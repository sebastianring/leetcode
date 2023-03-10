class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        #DO A BINARY SEARCH DUDE

        def bin_search(left, right):
            #print(f"target: {target}, left: {left}, right: {right}")
            if right==left:
                if target > nums[right]:
                    return right + 1
                else:
                    return right
            
            mid = (right+left) // 2
            if target > nums[mid]:
                return bin_search(mid+1, right)
            else:
                return bin_search(left, mid)

        return bin_search(0, len(nums)-1)
        
        

p = Solution()
print(p.searchInsert(nums = [1,3,5,6,7,8,9,10], target = 5)) # 2
print(p.searchInsert(nums = [1,3,5,6], target = 2)) # 1
print(p.searchInsert(nums = [1,3,5,6], target = 7)) # 4
print(p.searchInsert(nums = [1,3,5,6], target = 0)) # 0
print(p.searchInsert(nums = [2,3,4,8,10], target = 0)) # 0
