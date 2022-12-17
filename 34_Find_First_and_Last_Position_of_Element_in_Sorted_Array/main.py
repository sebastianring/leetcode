class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        length = len(nums)
        l = 0
        r = length-1
        mid = (r+l) // 2

        if length == 0 or target < nums[l] or target > nums[r]:
            return [-1, -1]
        elif length == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]
 
        while l < r:
            print(l, mid, r, nums[mid])
            if target == nums[mid]:
                break
            elif target < nums[mid]:
                r = mid
            else:
                l = mid+1

            mid = (r+l) // 2
            
        if nums[mid] == target:
            while nums[l] != target:
                l += 1
            while nums[r] != target:
                r -= 1
            return [l, r]

        else:
            return [-1, -1]


p = Solution()
print(f"{p.searchRange(nums = [5,7,7,8,8,10], target = 8)} expected: [3,4]")
print(f"{p.searchRange(nums = [5,7,7,8,8,10], target = 6)} expected: [-1,-1]")
print(f"{p.searchRange(nums = [], target = 0)} expected: [-1,-1]")
print(f"{p.searchRange(nums = [1], target = 1)} expected: [-1,-1]")
print(f"{p.searchRange(nums = [1,1,1,7,7,7,7,7,7,7,7,9,9,9,9,9,9,9,9,9,9,9,9,9], target = 7)} expected: [3,10]")
print(f"{p.searchRange(nums = [1,4], target = 4)} expected: [1, 1]")
print(f"{p.searchRange(nums = [1,2,3], target = 2)} expected: [1, 1]")
