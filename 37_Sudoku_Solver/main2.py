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
        dic_row = {}
        dic_col = {}
        dic_sqr = {}
        dic_score = {}

        for row in board:
            print(row)
        print("---------------------------------------------")

        # High level function to check all the available nums in one or many lists - Called in many different scenarios - squares, rows and columns with different inputs returns a list of available numbers
        def check_list(*lists: list) -> list:
            temp_nums = nums
            for list in lists:
                temp_nums = [x for x in temp_nums if x not in list]
            return temp_nums
        
        # Get the square which value lies in
        def get_square(col: int, row: int) -> tuple:
            x_factor = divmod(col, 3)[0] * 3
            y_factor = divmod(row, 3)[0] * 3

            return x_factor, y_factor

        # Get all available numbers from one row in the board
        def check_row(row: int) -> list:
            check_dic_row = dic_row.get(row, None)

            if check_dic_row:
                return check_dic_row
            else:
                r = check_list(board[row])
                dic_row[row] = r, len(r)
            
            return dic_row[row]
        
        # Get all available numbers from one column in the board
        def check_col(col: int) -> list:
            check_dic_col = dic_col.get(col, None)

            if check_dic_col:
                return check_dic_col
            else:
                r_list = [board[i][col] for i in range(9)]
                r = check_list(r_list)
                dic_col[col] = r, len(r)

            return dic_col[col]
        
        # Get all available numbers from one column in the board
        def check_square(col, row):
            x, y = get_square(col, row)
            check_dic_sqr = dic_sqr.get((x, y), None)

            if check_dic_sqr:
                return check_dic_sqr
            else:
                r_list = [board[y+i][x:x+3] for i in range(3)]
                r = check_list(r_list[0], r_list[1], r_list[2])
                dic_sqr[(x,y)] = r, len(r)

            return dic_sqr[(x,y)]

        def clear_dic():
            dic_row.clear()
            dic_col.clear()
            dic_sqr.clear()
        
        # get all numbers which are available for a certain coordinate
        def check_coords(x, y):
            temp_nums = nums
            row = check_row(y)[0]
            col = check_col(x)[0]
            sqr = check_square(x, y)[0]
            r_list = [val for val in temp_nums if val in row and val in col and val in sqr]
            return [r_list, len(r_list)]
        
        def update_vals_dic(val, x, y):
            if val in dic_col[x][0]:
                dic_col[x][0].remove(val)
                dic_col[x][1] -= 1
            if val in dic_row[y]:
                dic_row[y][0].remove(val)
                dic_row[y][1] -= 1
            
            square = get_square(x, y)
            if val in dic_sqr[square][0]:
                dic_sqr[square][0].remove(val)
                #dic_sqr[square][1] -= 1

        
        for y, row in enumerate(board):
             for x, val in enumerate(row):
                 if val == '.':
                    coords_val = check_coords(x, y)
                    if coords_val[1] == 1:
                        board[y][x] = coords_val[0][0]
                        update_vals_dic(coords_val[0][0], x, y)
                        print(x, y)
                    else:
                        dic_score[(x,y)] = coords_val
        

        for row in board:
            print(row)
        print("---------------SCORE-------------------------")
        
        for k, v in dic_score.items():
            print(k, v)
        print("---------------COLUMN------------------------")
        for k, v in dic_col.items():
            print(k, v)
        print("---------------ROW---------------------------")
        for k, v in dic_row.items():
            print(k, v)
        print("---------------SQUARE------------------------")
        for k, v in dic_sqr.items():
            print(k, v)


        #dic_score = {(y,x): check_coords(x, y) for y, row in enumerate(board) for x, val in enumerate(row) if val == '.'}

        # for y, row in enumerate(board):
        #     for x, val in enumerate(row):
        #         if val == '.':
                    #check_coords(x, y)
                    #print(f"{y, x}: {check_coords(x, y)}")

                    # print(f"CHECK ROW: {check_row(y)[0]}")
                    # print(f"CHECK COL: {check_col(x)[0]}")
                    # print(f"CHECK ROW: {check_square(x, y)[0]}")
                    # print(f"{y, x}: {check_list(check_row(y)[0], check_col(x)[0], check_square(x, y)[0])}")
            
        # print(dic_col)
        # print(dic_row)
        # print(dic_sqr)



p = Solution()
print(p.solveSudoku(board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))