import time


class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        print("   '0', '1', '2', '3', '4', '5', '6', '7', '8'")
        for number, row in enumerate(board):
            print(number, row)

        startTime = time.time()

        class SavePoint:
            def __init__(self, x: int = 0, y: int = 0, ctr: int = 0, threshold: int = 1):
                self.x = x
                self.y = y
                self.ctr = ctr
                self.threshold = threshold
                self.added = []

            def nextValue(self):
                if self.ctr == self.threshold-1:
                    if self.x < 8 and self.y < 9:
                        self.x += 1
                    elif self.x == 8 and self.y < 8:
                        self.y += 1
                        self.x = 0
                    else:
                        self.threshold += 1
                        self.ctr = 0
                else:
                    self.ctr += 1

        def printBoard():
            print("-----------------------------------------------")
            print("   '0', '1', '2', '3', '4', '5', '6', '7', '8'")
            for number, row in enumerate(board):
                print(number, row)

        def printSavepoints():
            for savePoint in savePoints:
                print('----SAVEPOINT-----',
                      f'x: {savePoint.x}x{savePoint.y}',
                      f'Threshold: {savePoint.threshold}',
                      f'Counter: {savePoint.ctr},'
                      f'Added: {len(savePoint.added)}'
                      )

        def checkAvailableNumbers(x: int, y: int, board: list[list[str]]):
            tempNums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

            # Check available numbers in row
            tempNums = [num for num in tempNums if num not in board[y]]

            # Check available numbers in col
            col = [board[i][x] for i in range(9)]
            tempNums = [num for num in tempNums if num not in col]

            # Check available numbers in sqr
            sqr_x = divmod(x, 3)[0] * 3
            sqr_y = divmod(y, 3)[0] * 3

            for i in range(sqr_y, sqr_y+3):
                tempNums = [num for num in tempNums if num not in board[i][sqr_x:sqr_x+3]]

            return tempNums, len(tempNums)

        gameOn = True
        savePoints = []
        currentSavePoint = SavePoint()
        savePoints.append(currentSavePoint)

        # Loop until board is solved
        while gameOn:
            gameOn = False

            for y in range(9):
                for x in range(9):
                    if board[y][x] != ".":
                        continue

                    availableNumbers, numbersCount = checkAvailableNumbers(x, y, board)
                    # print(f"x: {x}, y: {y}, availableNumbers: {availableNumbers}, {('-'*(25 - len(str(availableNumbers))))}currentSavePoint.ctr: {currentSavePoint.ctr}, currentSavePoint.threshold: {currentSavePoint.threshold}")

                    if numbersCount == 1:
                        gameOn = True
                        board[y][x] = availableNumbers[0]
                        currentSavePoint.added.append([x, y])

                    elif numbersCount == 0:
                        print(f"ZERO STARTED at x: {x}, y: {y} availableNumbers: {availableNumbers}")
                        printSavepoints()
                        print("-------------")
                        # print(f"trying to remove currentSavePoint: {currentSavePoint}")
                        for coords in currentSavePoint.added:
                            board[coords[1]][coords[0]] = "."
                            # print(f"REMOVING {coords[0]}, {coords[1]}")

                        # print(f"1:{currentSavePoint}, {currentSavePoint.ctr}, {currentSavePoint.threshold}")
                        del savePoints[-1]

                        currentSavePoint = savePoints[-1]
                        currentSavePoint.nextValue()

                        x = currentSavePoint.x
                        y = currentSavePoint.y
                        printSavepoints()
                        # print(f"2:{currentSavePoint}, {currentSavePoint.ctr}, {currentSavePoint.threshold}")

                    elif numbersCount <= currentSavePoint.threshold:
                        # print(f"availableNumbers: {availableNumbers} ctr: {currentSavePoint.ctr} ")
                        # print(f"TRYING {availableNumbers[currentSavePoint.ctr]} at x: {x} y: {y}")

                        board[y][x] = availableNumbers[currentSavePoint.ctr]

                        # printBoard()

                        currentSavePoint.x = x
                        currentSavePoint.y = y
                        currentSavePoint.nextValue()

                        p = SavePoint()
                        savePoints.append(p)
                        currentSavePoint = savePoints[-1]
                        currentSavePoint.added.append([x, y])

                        x = 0
                        y = 0

                        gameOn = False

            if gameOn is False:
                currentSavePoint.nextValue()
                # print(currentSavePoint.ctr, currentSavePoint.threshold, currentSavePoint.x, currentSavePoint.y)
                # printSavepoints()
                gameOn = True

                printBoard()

        #
        #
        #
        #
        #
        printBoard()
        print(savePoints[0].added)
        #
        #
        #
        #
        endTime = time.time()
        print(endTime-startTime)
        return


p = Solution()
# print(p.solveSudoku(board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))
print(p.solveSudoku(board = [[".",".","9","7","4","8",".",".","."],
                             ["7",".",".",".",".",".",".",".","."],
                             [".","2",".","1",".","9",".",".","."],
                             [".",".","7",".",".",".","2","4","."],
                             [".","6","4",".","1",".","5","9","."],
                             [".","9","8",".",".",".","3",".","."],
                             [".",".",".","8",".","3",".","2","."],
                             [".",".",".",".",".",".",".",".","6"],
                             [".",".",".","2","7","5","9",".","."]]))
