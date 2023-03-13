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

        class Board:
            def __init__(self, board: list[list[str]], threshold: int) -> None:
                self.board = board
                self.ctr = 0
                self.threshold = threshold

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
        boards = [Board(board, 1)]

        # Loop until board is solved
        while gameOn:
            # print(len(boards))
            currentBoard = boards[-1]
            breakFlag = False
            print(boards)
            print(f"This is currentBoard: {currentBoard}",
                    f"and its variables ctr: {currentBoard.ctr}",
                    f"and threshold: {currentBoard.threshold}")
            # board = currentBoard.board

            gameOn = False
            for y, row in enumerate(currentBoard.board):
                for x, num in enumerate(row):
                    if num != ".":
                        continue

                    availableNumbers, numbersCount = checkAvailableNumbers(x, y, currentBoard.board)

                    if numbersCount == 0:
                        print("BOARD REMOVED")
                        del boards[-1]
                        gameOn = True
                        breakFlag = True
                        break

                    elif numbersCount <= currentBoard.threshold:
                        if currentBoard.threshold > 1:
                            currentBoard.threshold = 1

                        gameOn = True
                        print(f'x: {x}, y: {y}, board ctr: {currentBoard.ctr}, availableNumbers {availableNumbers}')
                        currentBoard.board[y][x] = availableNumbers[currentBoard.ctr]

                if breakFlag:
                    break

            # If there is no obvious answer (only one option
            # for a specific cell), a guess is done
            if gameOn is False:
                print("------------- BOARD ADDED ------------------------")
                print("   '0', '1', '2', '3', '4', '5', '6', '7', '8'")
                for number, row in enumerate(currentBoard.board):
                    print(number, row)

                #
                #

                currentBoard.ctr += 1
                currentBoard.threshold += 1
                b = Board(board=currentBoard.board.copy(), threshold=2)
                boards.append(b)
                print(len(boards))
                gameOn = True

        #
        #
        #
        #
        #
        print("-----------------------------------------------")
        print("   '0', '1', '2', '3', '4', '5', '6', '7', '8'")
        for number, row in enumerate(board):
            print(number, row)

        #
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
