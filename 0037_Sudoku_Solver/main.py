# https://leetcode.com/problems/sudoku-solver/
#
# Write a program to solve a Sudoku puzzle by filling the empty cells.
#
# A sudoku solution must satisfy all of the following rules:
#
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.
# ----------------------------------------------------------------------------------------------

class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        rows = {}
        cols = {}

        for row in board:
            print(row)
        

        # Function to get all the available numbers for a specific COLUMN
        def availableNumbersCol(col: int) -> list:
            temp_nums = nums
            for i in range(9):
                #print(board[i][col])
                temp_nums = [x for x in temp_nums if x != board[i][col]]
            
            return temp_nums

        # Function to get all the available numbers in a specific ROW
        def availableNumbersRow(row: list) -> list:
            temp_nums = nums
            # Is just one or multiple rows?
            if isinstance(row[0], list):
                result = temp_nums
                
                for x in temp_nums:
                    for y in row:
                        if x in y:
                            result.remove(x)
                            break
                    

                # for y in row:
                #     for x in temp_nums:
                #         if x not in y:
                #             result.append(x)

            else:
                result = [x for x in temp_nums if x not in row]

            return result
        
        # Removes duplicates from two lists
        def removeDuplicates(list1: list, list2: list) -> list:
            return [elem for elem in list1 if elem not in list2]
        
        # Get the remaining available numbers based on all available slots in a column
        def availableNumbersFullCol(col: int) -> list:
            temp_nums = nums
            temp_list = []
            for i in range(9):
                if board[i][col] == '.':
                    print(board[i][col])
                    row = availableNumbersRow(board[i])
                    r = [x for x in temp_nums if x in row]
                    temp_list.append(r)
                    #print(f"tempnums: {temp_nums}")
                else:
                    if board[i][col] in temp_nums:
                        temp_nums.remove(board[i][col])
            
            return temp_list

        # Find the square a coordinate belongs to
        def getSquare(col: int, row: int) -> tuple:
            x_factor = divmod(col, 3)[0] * 3
            y_factor = divmod(row, 3)[0] * 3

            return x_factor, y_factor

        # Get the available numbers for the square the coordinate is placed in
        def availableNumbersSquare(col: int, row: int) -> list:
            x, y = getSquare(col, row)
            square_list = []

            for i in range(0, 3):
                r = board[y+i][x:x+3]
                square_list.append(r)
            
            r_nums = availableNumbersRow(square_list)
            print(f"NUMS: {r_nums}")
            
            return x, y

        print(f"Available nums: {availableNumbersSquare(1, 1)}")

        score_list_x = []
        score_list_y = []

        for x in range(9):
            col_score = availableNumbersCol(x)
            score_list_x.append(len(col_score))
            # r = [x, len(col_score)]
            # score_list_x.append(r)
        for y, row in enumerate(board):
            row_score = availableNumbersRow(row)
            score_list_y.append(len(row_score))
            # r = [y, len(row_score)]
            # score_list_y.append(r)

        min_val_x = min(score_list_x)
        min_index_x = score_list_x.index(min_val_x)

        min_val_y = min(score_list_y)
        min_index_y = score_list_y.index(min_val_y)

        #get values for x,y
        x_vals = availableNumbersRow(board[min_index_x])
        y_vals = availableNumbersCol(min_index_y)
        #print(x_vals, y_vals)

        #remove duplicates between lists
        remains = removeDuplicates(x_vals, y_vals)
        #print(remains)

        check_col = availableNumbersFullCol(4)
        #print(check_col)

        

        # total_list = zip(score_list_x, score_list_y)
        # for u in total_list:
        #     print(u)

        # min_x = min(score_list_x)
        # min_y = min(score_list_y)

        #print(min_x, min_y)

        


                



        # for idx, row in enumerate(board):
        #     vals = [x for x in row if x != '.']
        #     rows[idx] = vals
        
        # print(rows)
            



p = Solution()
print(p.solveSudoku(board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))