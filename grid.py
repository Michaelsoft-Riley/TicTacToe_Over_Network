class Grid:
    def __init__(self, slots, rows):
        slots = {
            (1,1): "",
            (1,2): "",
            (1,3): "",
            (2,1): "",
            (2,2): "",
            (2,3): "",
            (3,1): "",
            (3,2): "",
            (3,3): ""
        }
        # TODO: figure out an easy way to generate this so that I don't have to type them next time.
        rowv1 = {}
        rowv2 = {(2,1), (2,2), (2,3)}
        rowv3 = []
        rowh1 = []
        rowh2 = []
        rowh3 = []
        rowd1 = []
        rowd2 = []

    # Generate row values
    def row_generator(self):
        y = 1
        for x in range(1,4):
            self.rowv1.Add(x,y)
            y+=1

    # Checks whether a slot belongs to a team yet
    def is_available(self):
        if self.team == "":
            return True
    
    # Checks for three in a row of the same team from the selected slot (tuple)
    def is_win(self, slot):
        x = slot[0]
        y = slot[1]
        # Check if slot is a corner
        if (x == 1 or x == 3) and (y == 1 or y == 3):
            