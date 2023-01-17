#Third solution

class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        r_list = []
        cand_length = len(candidates)

        def rec_add(ctr=0, cur_sum=0, cur_list=[]):
            cur_sum+=candidates[ctr]
            cur_list.append(candidates[ctr])

            print(target, cur_sum, cur_list)
            for next_ctr in range(ctr+1, cand_length):
                if cur_sum + candidates[next_ctr] <= target:
                    rec_add(next_ctr, cur_sum, cur_list)

            if cur_sum + candidates[ctr] <= target:
                rec_add(ctr, cur_sum, cur_list)

            if cur_sum == target:
                r_list.append(cur_list)
            
            return

        for i in range(cand_length):
            rec_add(ctr=i)

        return r_list

            




p = Solution()
# print(p.combinationSum(candidates = [2, 3, 6, 7], target = 7))
# print(p.combinationSum(candidates = [2, 3, 5], target = 8))
# print(p.combinationSum(candidates = [8, 7, 4, 3], target = 11)) #[8, 3], [7, 4], [4,4,3]
print(p.combinationSum(candidates = [7, 3, 2], target = 18)) # [[7,7,2,2],[7,3,3,3,2],[7,3,2,2,2,2],[3,3,3,3,3,3],[3,3,3,3,2,2,2],[3,3,2,2,2,2,2,2],[2,2,2,2,2,2,2,2,2]]
