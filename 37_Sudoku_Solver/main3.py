class Solution:
    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        
        def defineSquare(x, y):
            x_factor = divmod(x, 3)[0]
            y_factor = divmod(y, 3)[0] * 3

            return x_factor + y_factor

        cols = []
        rows = []
        sqrs = []        
        elements = []

        print("---------START BOARD-----------")
        for row in board:
            print(row)
        print("-------------------------------")
        
        for y in range(9):
            new_row = Group("row", y)
            new_col = Group("col", y)
            new_sqr = Group("sqr", y)

            rows.append(new_row)
            cols.append(new_col)
            sqrs.append(new_sqr)

        for y, row in enumerate(board):
            for x, val in enumerate(row):
                sqr = defineSquare(x, y)
                if val == '.':
                    new_ele = Element(x, y, sqr)
                    cols[x].setLink(new_ele)
                    rows[y].setLink(new_ele)
                    sqrs[sqr].setLink(new_ele)
                    elements.append(new_ele)
                else:
                    cols[x].removeVal(val)
                    rows[y].removeVal(val)
                    sqrs[sqr].removeVal(val)

        game_on = True
        while game_on:
            elements_to_be_deleted = []
            game_on = False

            for element in elements:
                # print(f"---- ELEMENT {element.pos} ------")
                r = element.getAvailableNumbers()
                # print(r)
                if len(r) == 1:
                    board[element.y][element.x] = r[0]
                    element.removeValueFromGroup(r[0])
                    elements_to_be_deleted.append(element)
                    game_on = True
                # else:
                #     elements_remaining.append(element)

            for element in reversed(elements_to_be_deleted):
                elements.remove(element)
                element.destroy()
            #elements = elements_remaining

        for ctr, element in enumerate(elements):
            # print(ctr, element.pos)
            element.findOverlaps()
        
        print("---------END BOARD-------------")
        for row in board:
            print(row)
        
class Element:
    def __init__(self, x, y, sqr):
        self.x = x
        self.y = y
        self.sqr = sqr
        self.link = []
        self.available_numbers = []

    @property
    def pos(self):
        return self.x, self.y

    def getAvailableNumbers(self):
        temp_nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

        for link in self.link:
            temp_nums = [x for x in link.available_numbers if x in temp_nums]

        return temp_nums

    def findOverlaps(self):
        for link in self.link:
            elements = [self]
            available_numbers = self.getAvailableNumbers()

            for elem in link.links:
                if  available_numbers == elem.getAvailableNumbers() and self != elem:
                    # print("WE GOT A MATCH")
                    # print(self.pos, elem.pos)
                    elements.append(elem)
            
            if len(self.getAvailableNumbers()) == len(elements):
                print("WE GOT A SUPERMATCH - DELETE VALUES FROM OTHERS INSIDE THE SAME LINK")
                # for elem in elements:
                #     print(elem.getAvailableNumbers())
            else:
                return
            
            compare = []
            for elem in link.links:
                hit = True
                # compare = [x for self_num in available_numbers for x in elem.getAvailableNumbers() if x not in self_num]
                # compare = [x for x in elem.getAvailableNumbers() if x not in available_numbers]
                for x in available_numbers:
                    if x not in elem.getAvailableNumbers():
                        hit = True
                        break
                if hit:
                    compare.append(elem)
            print("-------COMPARE PRINT---------")
            for comp in compare:
                print(comp.getAvailableNumbers())
            print("-----------------------------")
            
        return

    def removeValueFromGroup(self, val):
        # print("BEFORE DELETE")
        # print(self.getAvailableNumbers())
        for link in self.link:
            # print(link.available_numbers)
            if val in link.available_numbers:
                link.available_numbers.remove(val)
        # print("AFTER DELETE")
        # print(self.getAvailableNumbers())

    def destroy(self):
        for link in self.link:
            link.links.remove(self)
        
        del self


class Group:
    def __init__(self, type, number) -> None:
        self.type = type        #col, sqr, row
        self.number = number
        self.available_numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.links = []

    def setLink(self, element):
        self.links.append(element)
        element.link.append(self)

    def removeVal(self, val):
        if val in self.available_numbers:
            self.available_numbers.remove(val)

    def defineSquare(self):
        x_factor = divmod(self.x, 3)[0]
        y_factor = divmod(self.y, 3)[0] * 3

        return x_factor + y_factor
    
p = Solution()
# print(p.solveSudoku(board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))
print(p.solveSudoku(board = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]))















    # @property
    # def row(self):
    #     return self.y
    
    # @property
    # def col(self):
    #     return self.x

    # @property
    # def link(self):
    #     return self._link

    # @link.setter
    # def linkSetter(self, group):
    #     self._link.append(group)


    
    # @property
    # def available_numbers(self):
    #     return self.available_numbers
    