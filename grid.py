class Grid:
    def __init__(self, slots, rows):
        # used to track which slots are owned by which team
        slots = {
            (1, 1): "",
            (1, 2): "",
            (1, 3): "",
            (2, 1): "",
            (2, 2): "",
            (2, 3): "",
            (3, 1): "",
            (3, 2): "",
            (3, 3): ""
        }

        # Team points for each row. (+or-)3 points = win. (rownumber: points)
        rowPoints = {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0
        }

        # vertical rows
        row1_v = {(1, 1), (1, 2), (1, 3)}
        row2_v = {(2, 3), (2, 1), (2, 2)}
        row3_v = {(3, 1), (3, 2), (3, 3)}
        # horizontal rows
        row4_h = {(3, 1), (1, 1), (2, 1)}
        row5_h = {(3, 2), (1, 2), (2, 2)}
        row6_h = {(2, 3), (3, 3), (1, 3)}
        # diagonal rows
        row7_d = {(1, 1), (2, 2), (3, 3)}
        row8_d = {[1, 3], (2, 2), (3, 1)}
        # all
        rows = [row1_v, row2_v, row3_v, row4_h, row5_h, row6_h, row7_d, row8_d]


    # Checks that a slot doesn't belong to a team yet
    def is_available(self, coordinate):
        if self.slots[coordinate] == "":
            return True
        

    # TODO: add check for win condition
    # If the slot coordinate is in a row, add a point for that team under the row in row_points
    # Accepts coordinate(tuple) and team(0 or 1)
    # X(0) points are negative, and O(1) points are positive
    def give_point(self, coordinate, team):
        for index, row in enumerate(self.rows):
            if coordinate in row:
                if team == 0:   
                    self.row_points[(index -1)] -= 1
                if team == 1:   
                    self.row_points[(index -1)] += 1
                
                # win condition
                # TODO: make this its own function. Also change the output depending on who won.
                if self.row_points[(index-1)] > 2:
                    print("Somebody won!")
                

    # TODO: both methods need is_available to be ran, so move it out of here and into a run() method or something 
    # Assigns slot to specified team if it is not taken. Takes an integer for team. (X=0, O=1)
    def assign_slot(self, coordinate, team):
        if self.is_available(coordinate):
            if team == 0:
                self.slots[coordinate] = "X"
            elif team == 1:
                self.slots[coordinate] = "O"
        else:
            print("I can't build here!")
    

    # Checks for three in a row

            

    # # Generate row values
    # def row_generator(self):
    #     for x in range(1,4):
    #         y = 1
    #         for i in range(1,4):
    #             if x == 1:
    #                 self.rowv1.add((x,y))
    #             elif x == 2:
    #                 self.rowv2.add((x,y))
    #             elif x == 3:
    #                 self.rowv3.add((x,y))
    #             y+=1
    #     for y in range(1,4):
    #         x = 1
    #         for i in range(1,4):
    #             if y == 1:
    #                 self.rowh4.add((x,y))
    #             elif y == 2:
    #                 self.rowh5.add((x,y))
    #             elif y == 3:
    #                 self.rowh6.add((x,y))
    #             x+=1