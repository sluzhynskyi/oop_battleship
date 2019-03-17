from field import Field
from player import Player


class Game:
    def __init__(self):
        """
        This method initializes a new instance of Game class.
        """
        self.__fields = [Field(), Field()]
        name1 = input("Player 1, input your name\n:")
        name2 = input("Player 2, input your name\n:")
        self.__players = [Player(name1), Player(name2)]
        self.__current_player = 1
        self.quantity = 0

    def read_position(self):
        """
        This method asks current player for the coordinates to shoot at and modifies a field
        :return: None
        """
        dots = []
        while True:
            (field_loc, field_my) = (self.__fields[1], self.__fields[0]) if self.__current_player == 1 \
                else (self.__fields[0], self.__fields[1])
            player_loc = self.__players[0] if self.__current_player == 1 else self.__players[1]
            user_input = player_loc.read_position()
            if isinstance(user_input, int):
                field_my.render_field(mode=user_input)
                break
            x, y = user_input
            ship_loc = field_loc.field[y][x]
            if not ship_loc.shoot_at((x, y)):
                self.__current_player = 2 if self.__current_player == 1 else 1
                field_loc.render_field()
                break
            else:
                if ship_loc.hit.count(True) == len(ship_loc.hit):
                    if self.player_win():
                        print("Congratulation %s, you are win" % player_loc.name)
                        break
                    x, y = ship_loc.bow
                    for ad in range(ship_loc.length):
                        if ship_loc.horizontal:
                            dots += [(num, y - 1) for num in range(x - 1 + ad, x + 2 + ad)] + \
                                    [(num, y) for num in range(x - 1 + ad, x + 2 + ad)] + \
                                    [(num, y + 1) for num in range(x - 1 + ad, x + 2 + ad)]
                        else:
                            dots += [(num, y + 1 + ad) for num in range(x - 1, x + 2)] + \
                                    [(num, y + ad) for num in range(x - 1, x + 2)] + \
                                    [(num, y - 1 + ad) for num in range(x - 1, x + 2)]
                        for ln in dots:
                            if ln[0] > -1 and ln[1] > -1:
                                try:
                                    field_loc.field[ln[1]][ln[0]].hit[0] = True
                                except IndexError:
                                    pass
            field_loc.render_field()

    def player_win(self):
        field_loc = self.__fields[1] if self.__current_player == 1 else self.__fields[0]
        import itertools
        flat = itertools.chain.from_iterable(field_loc.field)
        for ship_loc in flat:
            if ship_loc.ship_type:
                self.quantity += ship_loc.hit.count(True)
        if self.quantity == 50:
            return True
