class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while l < r:
            mid = (l + r) // 2
            #print(f"l: {l}, r: {r}, mid: {mid}")
            if nums[mid] == target:
                return mid
            if nums[mid] < nums[l] + (mid-l):
                #if this is true, then it MUST have been reset
                #print("trigger first if")
                if target == nums[l]:
                    return l
                elif target > nums[l] or target < nums[mid]:
                    r = mid
                else:
                    l = mid + 1
            else:
                #print("trigger 2nd if")
                if target == nums[l]:
                    return l
                elif target > nums[l]:
                    if target > nums[mid]:
                        l = mid + 1
                    else:
                        r = mid
                else:
                    l = mid + 1
            #print(f"l: {l}, r: {r}")

                

        if nums[l] == target:
            return l
        else:
            return -1


        print(r)

        pass


p = Solution()
print(p.search(nums = [4,5,6,7,0,1,2], target = 0)) #4
print(p.search(nums = [4,5,6,7,0,1,2], target = 3)) #-1
print(p.search(nums = [2,4,5,6,7,0,1], target = 3)) #-1
print(p.search(nums = [5,6,7,0,1,2,4], target = 3)) #-1
print(p.search(nums = [6,7,0,1,2,4,5], target = 3)) #-1
print(p.search(nums = [4,5,6,7,0,1,2], target = 2)) #6
# #                      0 1 2 3 4 5 6
print(p.search(nums = [1], target = 0)) #-1
print(p.search(nums = [1,3,5], target = 1)) #0
print(p.search(nums = [1,3,5], target = 5)) #2
print(p.search(nums = [5,1,3], target = 3)) #2
print(p.search(nums = [5,1,2,3,4], target = 1)) #1



# 679012