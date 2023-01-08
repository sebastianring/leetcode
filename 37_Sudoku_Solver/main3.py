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
       
        def setValue(element, val):
            board[element.y][element.x] = val
            element.removeValueFromGroup(val)
        areas = []

        cols = []
        rows = []
        sqrs = []

        areas.append(cols)
        areas.append(rows)
        areas.append(sqrs)

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
        ctr = 0
        game_on = True
        while game_on:
            elements_to_be_deleted = []
            game_on = False

            # -------- CHECK ELEMENTS --------
            for element in elements:
                r = element.getAvailableNumbers()
                if len(r) == 1:
                    setValue(element, r[0])
                    elements_to_be_deleted.append(element)
                    if game_on == False:
                            game_on = True

            for element in reversed(elements_to_be_deleted):
                elements.remove(element)
                element.destroy()

            if game_on == False:
                # --------- CHECK AREAS FOR UNIQUE VALUES ---------
                ctr += 1
                for area in areas:
                    for group in area:
                        elements_with_unique_num = group.getUniqueNumbers()
                        for element, val in elements_with_unique_num:
                            # print(element.x, element.y, val)
                            setValue(element, val)
                            elements_to_be_deleted.append(element)
                            if game_on == False:
                                game_on = True
               
                for element in reversed(elements_to_be_deleted):
                    elements.remove(element)
                    element.destroy()

                elements_to_be_deleted = []
           
            # if game_on == False:
            #     for ctr, element in enumerate(elements):
            #         # print(ctr, element.pos)
            #         element.findOverlaps()
            #         print(element.pos, element.getAvailableNumbers())

        # for ctr, element in enumerate(elements):
            # print(ctr, element.pos)
            # element.findOverlaps()
            # print(element.pos, element.getAvailableNumbers())
           

        # for area in areas:
        #     for group in area:
        #         group.getElementsWithOverlaps()
                # print(group.type, group.number)
                # for link in group.links:
                #     r = link.getAvailableNumbers()
                #     print(link.pos, r)
       
        print(sqrs[0].getElementsWithOverlaps())


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
        self.removed_numbers = []

    @property
    def pos(self):
        return (self.x, self.y)

    def getAvailableNumbers(self):
        temp_nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

        for val in self.removed_numbers:
            temp_nums.remove(val)

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
        for link in self.link:
            if val in link.available_numbers:
                link.available_numbers.remove(val)

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
   
    def getUniqueNumbers(self):
        number_count = {}

        for link in self.links:
            numbers = link.getAvailableNumbers()
            for number in numbers:
                check_number = number_count.get(number, None)
                if check_number == None:
                    number_count[number] = []
                    number_count[number].append(link)
                else:
                    number_count[number].append(link)
       
        r_list = [(val[0], key) for key, val in number_count.items() if len(val) == 1]

        return r_list
   
    def getElementsWithOverlaps(self):
        


        # A dictionary which writes how many times a number is present in a group and which elements have that value
        # {
        #   3: 2, (2, 1), (2, 2)            - 3 can be used in two different elements,      (2, 1) and (2, 2)
        #   4: 3, (1, 2), (0, 0), (0, 1)    - 4 can be used in three different elements,    (1, 2), (0, 0), (0, 1)
        # }
        # number_count = {}

        # for link in self.links:
        #     numbers = link.getAvailableNumbers()
        #     for number in numbers:
        #         check_number = number_count.get(number, None)
        #         if check_number == None:
        #             number_count[number] = [1]
        #             number_count[number].append(link)
        #         else:
        #             number_count[number][0] += 1
        #             number_count[number].append(link)
        
        # for k, values in number_count.items():

        # values_length_count = {values[0]: values[1:] for values in number_count.values()}
        # Creating a dictionary composed of number if different elements and the elements:
        # {
        #   3: [Element1, Element2, Element3], [Element4, Element5, Element6]
        # }
        # This can then be used to compare the different lists inside the values - if they are the same, then the values they contain can be removed the other elements in the total list

        # values_length_count = {values[0]: [vals[1:] for vals in number_count.values() if vals[0] == values[0]] for values in number_count.values()}

        # First - check if the values inside have the same length
        # for k, v in values_length_count.items():
        #     # print(k)
        #     for  in v:

        #         print(f"VALS: {vals}")            

        # for k, values in number_count.items():
        #     neededValuesForElement = values[0] + 1
        #     for i in range(1, neededValuesForElement):
        #         if neededValuesForElement != values[i].getAvailableNumbers():
        #             break
            

        # for k, values in number_count.items():
        #     print(k)
        #     for val in values:
        #         print(val)
            

        return 0
        # return number_count
        
       

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