class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for col in zip(*board):
            print(col)

        def isValidArray(*args: list):
            dic = {}
            print(args)
            for arg in args:
                for number in arg:
                    if number != ".":
                        existing = dic.get(number, None)
                        if existing:
                            # print(number)
                            return False
                        else:
                            dic[number] = 1
           
            # print(dic)

        # for j in range(0, 9, 3):
        #     # print(board[i][i:3], board[i+3][i:3], board[i+6][i:3])
        #     if isValidArray(board[j][j:], board[j+3][j:3], board[j+6][j+3]) == False:
        #         return False

        #squares
        for x in range(0, 7, 3):
            for y in range(0, 7, 3):
                rnge = x+3                
                if isValidArray(board[y][x:rnge],board[y+1][x:rnge], board[y+2][x:rnge]) == False:
                    return False
        
       #horizontal
        for row in board:
            if isValidArray(row) == False:
                return False
        
        #vertical
        for i in range(9):
            #print("HERE COMES VERTICAL")
            vertical_list = []
            for j in range(9):
                vertical_list.append(board[j][i])
            
            if isValidArray(vertical_list) == False:
                return False

        return True

p = Solution()
print(p.isValidSudoku(board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))
print(p.isValidSudoku(board = [["5","3",".",".","7",".","7",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))