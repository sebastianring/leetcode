class solution:
    def trap(self, height: list[int]) -> int:
        left = 0
        leftidx = 0
        # right = 0
        potentialvolume = 0
        resultvolume = 0

        print(height)

        for idx, num in enumerate(height):
            if num >= left:
                resultvolume += potentialvolume
                potentialvolume = 0

                left = num
                leftidx = idx

                print(f' high wall --- idx: {idx}, num: {num}, left: {left}, leftidx: {leftidx}, potentialvolume: {potentialvolume},              resultvolume: {resultvolume}')
            else:
                definitivevolume = potentialvolume - ((idx-leftidx-1)*(left-num))
                print('----------')
                print(f'defintive volume: {definitivevolume} = {potentialvolume} - (({idx}-{leftidx}-1)*({left}-{num}))')
                if definitivevolume > 0:
                    potentialvolume -= definitivevolume
                    resultvolume += definitivevolume

                potentialvolume += left-num
                print(f' low wall  --- idx: {idx}, num: {num}, left: {left}, leftidx: {leftidx}, potentialvolume: {potentialvolume}, defivole: {definitivevolume}, resultvolume: {resultvolume}')

        return resultvolume


r = solution()
# print(r.trap(height=[5, 4, 1, 2]))
# print(r.trap(height=[4, 2, 0, 3, 2, 5]))
print(r.trap(height=[4, 2, 0, 1, 2, 5]))
# print(r.trap(height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
