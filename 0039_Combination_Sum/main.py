class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        sum_dic = {}
        r_list = []

        def rec_addition(val: int, sum_of_vals: int, list_of_vals: list = []):
            if sum_dic.get(sum_of_vals, None) == None:
                sum_dic[sum_of_vals] = [] 
                sum_dic[sum_of_vals].append(list(list_of_vals))
            else:
                sum_dic[sum_of_vals].append(list(list_of_vals))

            diff = target-sum_of_vals
            if diff == 0:
                r_list.append(list_of_vals)
                return
            elif sum_dic.get(diff, None) != None:
                for vals in sum_dic[diff]:
                    r_list.append(list(list_of_vals + vals))
            
            if diff > sum_of_vals:
                list_of_vals.append(val)
                sum_of_vals += val
                return rec_addition(val, sum_of_vals, list_of_vals)
            
            return

        for value in candidates:
            rec_addition(value, value, [value])

        for k, v in sum_dic.items():
            print(k, v)


        return r_list 


p = Solution()
# print(p.combinationSum(candidates = [2, 3, 6, 7], target = 7))
# print(p.combinationSum(candidates = [2, 3, 5], target = 8))
# print(p.combinationSum(candidates = [8, 7, 4, 3], target = 11)) #[8, 3], [7, 4], [4,4,3]
print(p.combinationSum(candidates = [7, 3, 2], target = 18)) # [[7,7,2,2],[7,3,3,3,2],[7,3,2,2,2,2],[3,3,3,3,3,3],[3,3,3,3,2,2,2],[3,3,2,2,2,2,2,2],[2,2,2,2,2,2,2,2,2]]
