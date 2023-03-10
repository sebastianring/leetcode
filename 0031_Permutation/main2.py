#https://leetcode.com/problems/next-permutation/
#Do not return

class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        length = len(nums)
        lowest_val = nums[-1]

        for i in range(length, 0, -1):
            if lowest_val > nums[i]:
                lowest_val = nums[i]
            options = [val for val in nums[i:] if val > nums[i]]
            if options:
                min_val = min(options)
                

p = Solution()
# print(p.nextPermutation(nums = [1,2,3]))
# print(p.nextPermutation(nums = [1,3,2]))
# print(p.nextPermutation(nums = [1,3,2,2]))
# print(p.nextPermutation(nums = [1,3,2,2,4,1,5]))
# print(p.nextPermutation(nums = [3,2,1]))
# print(p.nextPermutation(nums = [2,3,1]))
# print(p.nextPermutation(nums = [1,1,5]))
# print(p.nextPermutation(nums = [1,2,3,4]))
# print(p.nextPermutation(nums = [4,4,4,4]))
# print(p.nextPermutation(nums = [99,10,51,45,2,7,10]))
print(p.nextPermutation(nums = [5,4,7,5,3,2])) #  [5,5,2,3,4,7]