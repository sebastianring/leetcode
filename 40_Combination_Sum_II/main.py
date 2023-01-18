# https://leetcode.com/problems/combination-sum-ii/
# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
# Each number in candidates may only be used once in the combination.
# Note: The solution set must not contain duplicate combinations.

# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]

# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]



class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        cand_length = len(candidates)
        candidates.sort() 
        r_list = []

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
                latest_number = -1
                for nextctr in range(ctr+1, cand_length):
                    if candidates[nextctr] != latest_number:
                        next_sum = cur_sum + candidates[nextctr]
                        if next_sum <= target:
                            latest_number = candidates[nextctr]
                            new_list = list(cur_list)
                            new_list.append(candidates[nextctr])
                            rec_add(nextctr, next_sum, new_list)
                        else:
                            break

        last_number = -1

        for i in range(cand_length):
            if candidates[i] <= target:
                if last_number != candidates[i]:
                    last_number = candidates[i]
                    rec_add(i, candidates[i])
            else:
                break


        
        return r_list

            




p = Solution()
print(p.combinationSum2(candidates = [2,5,2,1,2], target = 5))
print(p.combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8))
