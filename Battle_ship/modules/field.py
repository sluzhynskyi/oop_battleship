from random import randint
from ship import Ship


class Field:
    def __init__(self):
        """
        This class for initializing new Fields instance.
        """
        self.field = self.field_generation()

    @staticmethod
    def field_generation():
        """

        :return: data
        """

        def valid(ships_lst, x, y, length, horizontal):
            """
            :param ships_lst: lst
            :param x: int
            :param y: int
            :param length: int
            :param horizontal: bool
            :return: bool
            """
            dots = []
            for ad in range(length):
                if horizontal:
                    if x + length > 10:
                        return False
                    dots += [(num, y - 1) for num in range(x - 1 + ad, x + 2 + ad)] + \
                            [(num, y) for num in range(x - 1 + ad, x + 2 + ad)] + \
                            [(num, y + 1) for num in range(x - 1 + ad, x + 2 + ad)]
                else:
                    if y + length > 10:
                        return False
                    dots += [(num, y + 1 + ad) for num in range(x - 1, x + 2)] + \
                            [(num, y + ad) for num in range(x - 1, x + 2)] + \
                            [(num, y - 1 + ad) for num in range(x - 1, x + 2)]
                for ln in dots:
                    try:
                        if ships_lst[ln[1]][ln[0]].ship_type:
                            return False
                    except IndexError:
                        pass
            s = Ship(x, y, horizontal, True, length)
            for i in range(length):
                if horizontal:
                    ships_lst[y][x + i] = s
                else:
                    ships_lst[y + i][x] = s
            return True

        ships_lst = [[Ship(y, x, 1, False, 1) for x in range(10)] for y in
                     range(10)]
        st = True
        for length_i in [4, 3, 3, 2, 2, 2, 1, 1, 1, 1]:
            while st or not valid(ships_lst, x, y, length_i, horizontal):
                x, y, horizontal = randint(0, 9), randint(0, 9), randint(0, 1)
                st = False
        return ships_lst

    def render_field(self, mode=0):
        """
        prints to user field
        :param mode: int
        :return: None
        """
        print("|  |a|b|c|d|e|f|g|h|i|j|")
        for y in range(10):
            print("|{:2d}|".format(y + 1), end="")
            for x in range(10):
                print(self.field[x][y].render(x, y, mode), end="|")
            print()
