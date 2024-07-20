class Grid:
    # TODO: FIX: opponent ai only checks for available slots in a single row. This can lead to the opponent 
    #       not selecting a slot during their turn.
    # TODO: option to play with other players (remember to add a check before running ai-player select)
    win = ""

    # used to track which slots are owned by which team
    slots = {
        (1, 1): "|",
        (1, 2): "|",
        (1, 3): "|",
        (2, 1): "|",
        (2, 2): "|",
        (2, 3): "|",
        (3, 1): "|",
        (3, 2): "|",
        (3, 3): "|"
    }

    # Team points for each row. + or - 3 points is a win. (rownumber: points)
    # Team X is negative points, and team O is positive.
    row_points = {
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
    row8_d = {(1, 3), (2, 2), (3, 1)}
    # all
    rows = [row1_v, row2_v, row3_v, row4_h, row5_h, row6_h, row7_d, row8_d]


    # Accepts an (x,y) coordinate as a tuple.
    # Takes an integer for team. (X=0, O=1)
    # Gives the team a point on each row that contains (coordinate).
    # Returns the current grid
    def select_slot(self, coordinate, team):
        if self.is_available(coordinate):
            self.assign_slot(coordinate, team)
            self.give_point(coordinate, team)
        else:
            print("I can't build here!")


    # Checks that a slot doesn't belong to a team yet
    def is_available(self, coordinate):
        if self.slots[coordinate] == "|":
            return True
        

    # Assigns slot to specified team if it is not taken. Takes an integer for team. (X=0, O=1)
    def assign_slot(self, coordinate, team):
            if team == 0:
                self.slots[coordinate] = "X"
            elif team == 1:
                self.slots[coordinate] = "O"


    # If the slot coordinate is in a row, add a point for that team under the row in row_points
    # Each time a point is added is_win and is_draw are used to check whether the game should end.
    # Accepts coordinate(tuple) and team(0 or 1)
    # X(0) points are negative, and O(1) points are positive
    def give_point(self, coordinate, team):
        for index, row in enumerate(self.rows):
            if coordinate in row:
                # key for the related row in row_points
                points_key = index + 1
                if team == 0:   
                    self.row_points[(points_key)] -= 1
                elif team == 1:   
                    self.row_points[(points_key)] += 1
                
                # Check for victory
                if self.is_win(points_key):
                    return
        # Check for draw
        if self.is_draw():
            return
    

    # Checks for three in a row
    def is_win(self, points_key):
        if self.row_points[(points_key)] > 2:
            print("Team O wins!")
            self.win = "O"
            return True
        elif self.row_points[(points_key)] < -2:
            print("Team X wins!")
            self.win = "X"
            return True
        

    def is_draw(self):
        for key in self.slots:
            if self.slots[key] == "|":
                return False
        self.win = "DRAW"
        print("Draw!")
        return True


    # TODO: Only adjust the string for each new slot assignment, instead of always generating it from scratch.
    # returns the team value for each slot in the grid as a list of chars in order
    def get_progress(self):
        progress = ""
        progress += self.slots[1,1]
        progress += self.slots[1,2]
        progress += self.slots[1,3]
        progress += self.slots[2,1]
        progress += self.slots[2,2]
        progress += self.slots[2,3]
        progress += self.slots[3,1]
        progress += self.slots[3,2]
        progress += self.slots[3,3]
        return progress
    

    # TODO: opponent should only be ran if user's choice was available
    # TODO: choose randomly between best choices
    # TODO: choose the center if user chooses edge and does not have 2 points in a row yet?
    # selects a coordinate in a row where team X has the most points
    def opponent(self):
        # team X has negative points, so we want the row with the lowest points
        lowest = 0
        index = 0
        for i in range(1,9):
            if self.row_points[i] < lowest:
                lowest = self.row_points[i]
                index = i-1

        # find an available slot and take it
        row = self.rows[index]
        for coord in row:
            if self.slots[coord] == "|":
                self.select_slot(coord, 1)
                return
            
    
    def reset(self):
        self.win = ""
        self.slots = {
            (1, 1): "|",
            (1, 2): "|",
            (1, 3): "|",
            (2, 1): "|",
            (2, 2): "|",
            (2, 3): "|",
            (3, 1): "|",
            (3, 2): "|",
            (3, 3): "|"
        }
        self.row_points = {
            1: 0,
            2: 0,
            3: 0,
            4: 0,
            5: 0,
            6: 0,
            7: 0,
            8: 0
        }
            

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