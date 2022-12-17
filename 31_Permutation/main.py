#https://leetcode.com/problems/next-permutation/
#Do not return

class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        record = 0
        iter = 0

        min = nums[-1]
        length = len(nums)-1
        closest = 101

        for i in range(length, 0, -1):
            if nums[i] < min:
                min = nums[i]

            check = nums[i]-nums[0]
            if check > 0 and check < closest:
                closest = nums[i]
                closest_i = i
            
            if min > nums[i-1]:
                a = nums[i-1]
                nums[i-1] = min
                min = a
                for j in range(i, length+1):
                    if min < nums[j]:
                        a = nums[j]
                        nums[j] = min
                        min = a
                        
                    if j == length-1:
                        nums[length] = min
                
                break
            
            if i == 1 and closest == 101:
                nums.reverse()
                break
            elif i == 1:
                a = nums[0]
                nums[0] = closest
                nums[closest_i] = a
                for j in range(i, length+1):
                    if min < nums[j]:
                        a = nums[j]
                        nums[j] = min
                        min = a
                        
                    if j == length-1:
                        nums[length] = min

        print(f"record: {record}, iter: {iter}, nums: {nums}")


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
print(p.nextPermutation(nums = [5,4,7,5,3,2]))
# [5,5,2,3,4,7]
