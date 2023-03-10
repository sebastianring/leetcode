#Test:w
class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        calculated_values = {} 
        r_list = []

        def rec_add(val):
            power = divmod(target, val)[0]

            for i in range(1, power+1):
                add_value = val*i
                if calculated_values.get(add_value, None) == None:
                    calculated_values[add_value] = []
                list_of_vals = [val for j in range(1, i+1)]
                calculated_values[add_value].append(list_of_vals)

                if add_value != target:
                    for k, v in calculated_values.items():
                        additions = add_value+k
                        if additions <= target:
                            if calculated_values.get(additions, None) == None:
                                calculated_values[additions] = []
                            calculated_values[additions].append([list_of_vals + vals for vals in v])

       

                diff = target-add_value
                # print(f'DIFF: {diff} ADD VAL: {add_value} VAL : {val}')
                if calculated_values.get(diff, None):
                    temp_list = [list_of_vals+vals for vals in calculated_values[diff]]
                    # print(f'TEMP LIST: {temp_list} KEY LIST: {calculated_values[diff]}')

                    for tlist in temp_list:
                        if tlist not in r_list:
                            r_list.append(tlist)

        for val in candidates:
            rec_add(val)

        # print(calculated_values)

        # for k, v in calculated_values.items():
            # diff = target-k
            # if v != -100 and calculated_values.get(diff, None): 
                # temp_list = [list(vals+vals2) for vals in v for vals2 in calculated_values[diff]]
                # r_list.append(temp_list)
                # calculated_values[diff] = -100
                # v = -100

        return r_list






















p = Solution()
# print(p.combinationSum(candidates = [2, 3, 6, 7], target = 7))
# print(p.combinationSum(candidates = [2, 3, 5], target = 8))
# print(p.combinationSum(candidates = [8, 7, 4, 3], target = 11)) #[8, 3], [7, 4], [4,4,3]
print(p.combinationSum(candidates = [7, 3, 2], target = 18)) # [[7,7,2,2],[7,3,3,3,2],[7,3,2,2,2,2],[3,3,3,3,3,3],[3,3,3,3,2,2,2],[3,3,2,2,2,2,2,2],[2,2,2,2,2,2,2,2,2]]
