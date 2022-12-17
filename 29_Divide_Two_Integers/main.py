class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend >= 0 and divisor >= 0 or dividend < 0 and divisor < 0:
            posi = True
        else:
            posi = False
        
        dividend = abs(dividend)
        divisor = abs(divisor)

        if divisor <= dividend:
            count = 1
            sum = divisor
        else:
            return 0

        sums = []

        while sum + divisor <= dividend:
            if (sum + sum) <= dividend:
                ele = (count+count, sum+sum)
                sums.append(ele)
                sum += sum
                count += count
            else:
                length = len(sums)
                if length > 0:
                    for i in range(length-1, -1, -1):
                        if sums[i][1] + sum <= dividend:
                            count += sums[i][0]
                            sum += sums[i][1]
                        else:
                            del sums[i]
                else:
                    count += 1
                    sum += divisor
        
        if posi == False:
            count = -count

        if count > 2147483647:
            count = 2147483647
        elif count < -2147483648:
            count = -2147483648
        
        return count


p = Solution()
print(f"{p.divide(dividend = 10, divisor = 3)} expected: 3")
print(f"{p.divide(dividend = 7, divisor = -3)} expected: -2")
print(f"{p.divide(dividend = -1, divisor = 1)} expected: -1")
print(f"{p.divide(dividend = -2147483648, divisor = -1)} expected: 2147483647")
print(f"{p.divide(dividend = 2147483647, divisor = 1)} expected: 2147483647")
# print(p.divide(dividend = 7, divisor = -3))