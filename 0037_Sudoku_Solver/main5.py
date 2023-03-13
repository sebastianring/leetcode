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
            def __init__(self, ctr=0, threshold=1):
                self.ctr = ctr
                self.threshold = threshold
                self.added = []

        def printBoard():
            print("-----------------------------------------------")
            print("   '0', '1', '2', '3', '4', '5', '6', '7', '8'")
            for number, row in enumerate(board):
                print(number, row)


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
        threshold = 1
        savePoints = []
        currentSavePoint = None

        # Loop until board is solved
        while gameOn:
            gameOn = False

            if currentSavePoint:
                ctr = currentSavePoint.ctr
                threshold = currentSavePoint.threshold
            else:
                ctr = 0
                threshold = 1

            for y in range(9):
                for x in range(9):
                    if board[y][x] != ".":
                        continue

                    availableNumbers, numbersCount = checkAvailableNumbers(x, y, board)

                    if numbersCount == 0:
                        for coord in currentSavePoint.added:
                            board[coord[1]][coord[0]] = "."

                        if currentSavePoint.ctr == currentSavePoint.threshold:
                            del savePoints[-1]

                            currentSavePoint = savePoints[-1]
                            currentSavePoint.ctr += 1
                        else:
                            currentSavePoint.ctr += 1

                        print(f'ABORTED -- savePoints left: {savePoints}')
                        # printBoard()

                        # currentSavePoint = savePoints[-1]
                        # currentSavePoint.ctr += 1

                        y = 10
                        x = 10

                    elif numbersCount <= threshold:
                        if ctr > 0:
                            print(ctr, currentSavePoint)

                        if gameOn is False:
                            gameOn = True

                        board[y][x] = availableNumbers[ctr]
                        if currentSavePoint:
                            currentSavePoint.added.append([x, y])

            # if len(currentSavePoint.added) == 0:
            #     del currentSavePoint
            #     currentSavePoint = savePoints[-1]

            if gameOn is False:
                p = SavePoint(ctr=0, threshold=2)
                savePoints.append(p)
                currentSavePoint = p
                gameOn = True

        #
        #
        #
        #
        #
        printBoard()
        #
        #
        #
        #
        endTime = time.time()
        print(endTime-startTime)
        return


p = Solution()
# print(p.solveSudoku(board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))
print(p.solveSudoku(board = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]))
