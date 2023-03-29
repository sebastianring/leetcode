class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
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

        def gameOn() -> bool:
            for row in board:
                if "." in row:
                    return True

            return False

        def recursiveGuess(board: list[list[str]], threshold: int = 1, addedVal: list[int] = []) -> bool:
            added = addedVal.copy()
            guess = False

            while gameOn():
                y = 0
                while y < 9:
                    x = 0
                    while x < 9:
                        if board[y][x] != ".":
                            x += 1
                            continue

                        availableNumbers, numbersCount = checkAvailableNumbers(x=x, y=y, board=board)

                        if numbersCount == 1:
                            board[y][x] = availableNumbers[0]
                            added.append([x, y])
                            x = 0
                            y = 0

                        elif numbersCount == 0:
                            for num in added:
                                board[num[1]][num[0]] = "."

                            return False

                        elif guess:
                            guess = False

                            for num in availableNumbers:
                                board[y][x] = num
                                if recursiveGuess(board=board, addedVal=[[x, y]]):
                                    return True

                            for num in added:
                                board[num[1]][num[0]] = "."

                            return False

                        x += 1
                    y += 1

                guess = True

            return True

        recursiveGuess(board=board)

        return board


p = Solution()
print(p.solveSudoku(board=[
            [".",".","9","7","4","8",".",".","."],
            ["7",".",".",".",".",".",".",".","."],
            [".","2",".","1",".","9",".",".","."],
            [".",".","7",".",".",".","2","4","."],
            [".","6","4",".","1",".","5","9","."],
            [".","9","8",".",".",".","3",".","."],
            [".",".",".","8",".","3",".","2","."],
            [".",".",".",".",".",".",".",".","6"],
            [".",".",".","2","7","5","9",".","."]]))
