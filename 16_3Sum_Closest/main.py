class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()

        return nums


p = Solution()

print(p.threeSumClosest(nums=[-1, 2, 1, -4], target=1))
print(p.threeSumClosest(nums=[0, 0, 0], target=1))
