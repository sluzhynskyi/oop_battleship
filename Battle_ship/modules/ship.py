class Ship:
    def __init__(self, x, y, horizontal, ship_type, length):
        """

        :param x: int
        :param y: int
        :param horizontal: int 0 or 1
        :param ship_type: bool
        :param length: int
        """
        self.bow = (x, y)
        self.horizontal = horizontal
        self.ship_type = ship_type
        self.length = length
        self.hit = [False] * length

    def render(self, x, y, mode=0):
        """
        This method for render ship demands of command (field_without_ships or field_with_ships) or standard
        :param x: int
        :param y: int
        :param mode: int
        :return: str
        """
        if not mode:  # Standard field render
            if self.ship_type:
                ind = x - self.bow[0] + y - self.bow[1]
                return "X" if self.hit[ind] else " "
            else:
                return "*" if self.hit[0] else " "
        elif mode == 1:  # Field with ships
            if self.ship_type:
                return "X"
            return "*" if self.hit[0] else " "
        else:  # Field without ships
            if not self.ship_type:
                return "*" if self.hit[0] else " "
            ind = x - self.bow[0] + y - self.bow[1]  # Index of wounded part of ship
            return "*" if self.hit[ind] else " "

    def shoot_at(self, coord):
        """
        This method takes coordinates of ship and makes it damaged and returns True if ship damaged
        :param coord:
        :return: bool
        """
        x, y = coord
        if self.ship_type:
            ind = x - self.bow[0] + y - self.bow[1]
            if not self.hit[ind]:
                self.hit[coord[0] - self.bow[0] + coord[1] - self.bow[1]] = True
                return True
        self.hit[0] = True
        return False
