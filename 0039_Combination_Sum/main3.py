#Third solution

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        r_list = []
        cand_length = len(candidates)

        def rec_add(ctr: int, cur_sum: int, cur_list=None):
            if cur_list==None:
                cur_list = []
                cur_list.append(candidates[i])

            if cur_sum==target:
                r_list.append(cur_list)
                return
            elif cur_sum > target:
                return
            else:
                for nextctr in range(ctr, cand_length):
                    next_sum = cur_sum + candidates[nextctr]
                    if next_sum <= target:
                        new_list = list(cur_list)
                        new_list.append(candidates[nextctr])
                        rec_add(nextctr, next_sum, new_list)


        for i in range(cand_length):
            rec_add(i, candidates[i])

        return r_list

            




p = Solution()
print(p.combinationSum(candidates = [2, 3, 6, 7], target = 7))
print(p.combinationSum(candidates = [2, 3, 5], target = 8))
print(p.combinationSum(candidates = [8, 7, 4, 3], target = 11)) #[8, 3], [7, 4], [4,4,3]
print(p.combinationSum(candidates = [7, 3, 2], target = 18)) # [[7,7,2,2],[7,3,3,3,2],[7,3,2,2,2,2],[3,3,3,3,3,3],[3,3,3,3,2,2,2],[3,3,2,2,2,2,2,2],[2,2,2,2,2,2,2,2,2]]
