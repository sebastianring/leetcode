class solution:
    def trap(self, height: list[int]) -> int:
        left = 0
        leftWall = height[left]

        right = len(height)-1
        rightWall = height[right]

        resultVolume = 0

        # print(height)

        while left < right:
            # print(f'l: {left},'
            #       f'r: {right}, {"-"*(10-len(str(right)))} '
            #       f'lW: {leftWall},'
            #       f'rW: {rightWall},'
            #       f'rV: {resultVolume}')

            if height[right] > height[left]:
                movingLeft = True
                left += 1
            else:
                movingLeft = False
                right -= 1

            lowestWall = min(leftWall, rightWall)

            if movingLeft:
                if height[left] >= leftWall:
                    leftWall = height[left]

                else:
                    definitiveVolume = max((lowestWall-height[left]), 0)
                    resultVolume += definitiveVolume
            else:
                if height[right] >= rightWall:
                    rightWall = height[right]

                else:
                    definitiveVolume = max((lowestWall-height[right]), 0)
                    resultVolume += definitiveVolume

        return resultVolume


r = solution()
print(r.trap(height=[5, 4, 1, 2]))
print(r.trap(height=[4, 2, 0, 3, 2, 5]))
print(r.trap(height=[0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
