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
        def check_square(col: int, row: int) -> None:
            x, y = get_square(col, row)
            check_dic_sqr = dic_sqr.get((x, y), None)

            if check_dic_sqr:
                return check_dic_sqr
            else:
                r_list = [board[y+i][x:x+3] for i in range(3)]
                r = check_list(r_list[0], r_list[1], r_list[2])
                dic_sqr[(x,y)] = r, len(r)

            return dic_sqr[(x,y)]

        # Get all numbers which are available for a certain coordinate
        def check_coords(x: int, y: int) -> list:
            temp_nums = nums
            row = check_row(y)[0]
            col = check_col(x)[0]
            sqr = check_square(x, y)[0]
            r_list = [val for val in temp_nums if val in row and val in col and val in sqr]
            return [r_list, len(r_list)]
        
        # Update the dictionary
        def update_score_dic(val: int, x: int, y: int) -> None:
            square_x, square_y = get_square(x, y)

            for i in range(9):
                # Remove square values
                if i < 3:
                    for j in range(3):
                        if dic_score.get((square_x+j, square_y+i), None):
                            if val in dic_score[(square_x+j, square_y+i)][0]:
                                dic_score[(square_x+j, square_y+i)][0].remove(val)
                                dic_score[(square_x+j, square_y+i)][1] -= 1
                                # print(f"VALUE REMOVED: {val} from {(i, y)}")
                
                # Remove x axis values
                if dic_score.get((i, y), None):
                    if val in dic_score[(i, y)][0]:
                        dic_score[(i, y)][0].remove(val)
                        dic_score[(i, y)][1] -= 1
                        # print(f"VALUE REMOVED: {val} from {(i, y)}")

                # Remove y axis values
                if dic_score.get((x, i), None):
                    if val in dic_score[(x, i)][0]:
                        dic_score[(x, i)][0].remove(val)
                        dic_score[(x, i)][1] -= 1
                        # print(f"VALUE REMOVED: {val} from {(x, i)}")
                
        # Get all relevant coords
        def get_affected_coords(x: int, y: int) -> tuple:
            coords = []

            for i in range(9):
                if i != y:
                    x_coord = dic_score.get((x, i), None)
                    if x_coord:
                        coords.append((x, i))

                if i != x:
                    y_coord = dic_score.get((i, y), None)
                    if y_coord:
                        coords.append((i, y))

            square_x, square_y = get_square(x, y)
            
            for i in range(3):
                for j in range(3):
                    if square_x+i != x and square_y+j != y:
                        sqr_coord = dic_score.get((square_x+i, square_y+j), None)
                        if sqr_coord:
                            coords.append((square_x+i, square_y+j))
            
            return coords
        
        # Deletes overlapping values for relevant elements, e.g. element #1 options: [3, 5], and element #2s options:
        def delete_overlaps(x: int, y: int) -> None:
            removed_list = []
            compared_coords = get_affected_coords(x, y)

            if does_equal_vals_exist((x, y), compared_coords):
                vals = dic_score[(x,y)][0]
                left_coords, common_coords = remove_equal_coords((x, y), vals, compared_coords)
                find_common_areas(common_coords, left_coords)
            
                for val in vals:
                    for key in left_coords:
                        if val in dic_score[key][0]:
                            dic_score[key][0].remove(val)
                            if dic_score[key][1] == 1:
                                removed_list.append(key)
                            else:
                                dic_score[key][1] -= 1

            return removed_list       

        # Compare one coords val to relevant coords, if equal values exist in another key, then return true, else return false
        def does_equal_vals_exist(one_coord: tuple, coords_list: list) -> bool:
            ctr = 1
            for coord in coords_list:
                # print(f'ONE: {dic_score[one_coord][0]} COORD: {dic_score[coord][0]}')
                if dic_score[one_coord][0] == dic_score[coord][0]:
                    ctr += 1
                
            if ctr == len(dic_score[one_coord][0]):
                print("YES TRUE BOI")
                return True
            else:
                print("NO FALSE BOI")
                print(ctr, len(dic_score[one_coord][0]))
                return False
        
        # Removes coordinates in a list which have the same values, part of delete_overlaps
        def remove_equal_coords(original: tuple, vals: list, coords_list: list):
            commons = [original]
            left = []
            for coords in coords_list:
                if dic_score[coords][0] == vals:
                    commons.append(coords)
                else:
                    left.append(coords)
            # r_list = [coords for coords in coords_list if dic_score[coords][0] != vals]

            return left, commons

        # Find the common areas and remove the ones which are not common
        def find_common_areas(common, left):
            print("COMMON VALUES")
            for c in common:
                print(c)

            print("LEFT VALUES")
            for l in left:
                
                print(l)


        # Initialize the score dictionary
        for y, row in enumerate(board):
             for x, val in enumerate(row):
                 if val == '.':
                    coords_val = check_coords(x, y)
                    dic_score[(x,y)] = coords_val
        
        # Play the game
        game_on = True
        low = 1

        while game_on:
            game_on = False
            keys_to_del = []
            for (x, y), v in dic_score.items():
                
                #Only one option - place those
                if v[1] == 1:
                    coords_val = v[0][0]
                    update_score_dic(coords_val, x, y)
                    board[y][x] = coords_val
                    keys_to_del.append((x, y))
                    game_on = True

            # Clean up activity
            for key in keys_to_del:
                del dic_score[key]

            # if game_on == False and len(dic_score) > 0:
            #     for (x, y), v in dic_score.items():
            #         delete_overlaps(x, y)
                
            #     game_on = True
            

            print("---------------SCORE-------------------------")
            for k, v in dic_score.items():
                # print(k[1], k[0], v)
                print(k, v)
        
        # for (x, y), v in dic_score.items():
        #     print(x, y)
        #     r = delete_overlaps(x, y)
        #     if len(r) > 0:
        #         print(f'DELETING OVERLAPS AT {x} and {y}')
        #         break

        delete_overlaps(4, 1)
        delete_overlaps(1, 0)

        for row in board:
            print(row)

        print("---------------SCORE-------------------------")
        for k, v in dic_score.items():
            print(k, v)

        # coord = (4, 1)
        # coords_list = get_affected_coords(coord[0], coord[1])
        # for co in coords_list:
        #     print(co)
        
        # print("---------------DIVIDER-------------------------")

        # delete_overlaps(coord[0], coord[1])
        # coords_list = get_affected_coords(coord[0], coord[1])
        # for co in coords_list:
        #     print(co)
        
        # print("---------------SCORE-------------------------")
        # for k, v in dic_score.items():
        #     print(k, v)





        # print("---------------COLUMN------------------------")
        # for k, v in dic_col.items():
        #     print(k, v)
        # print("---------------ROW---------------------------")
        # for k, v in dic_row.items():
        #     print(k, v)
        # print("---------------SQUARE------------------------")
        # for k, v in dic_sqr.items():
        #     print(k, v)


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

        # Update the dictionary
        # def update_vals_dic(val: int, x: int, y: int) -> None:
        #     if val in dic_col[x][0]:
        #         dic_col[x][0].remove(val)
        #         #dic_col[x][1] -= 1
            
        #     if val in dic_row[y]:
        #         dic_row[y][0].remove(val)
        #         # dic_row[y][1] -= 1
            
        #     square = get_square(x, y)
        #     if val in dic_sqr[square][0]:
        #         dic_sqr[square][0].remove(val)
        #         #dic_sqr[square][1] -= 1





p = Solution()
# print(p.solveSudoku(board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))
print(p.solveSudoku(board = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]))