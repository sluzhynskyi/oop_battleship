from field import Field


class Player:
    def __init__(self, name):
        """
        This method initializes a new Player
        """
        self.name = name

    def read_position(self):
        """
        This method asks Player for the coord to shoot at,read-modify and returns it a tuple.
        If Player inputs command return int
        :return: tuple or int
        """
        while True:
            try:
                prompt = self.name + " input command or coordinates\ncommands:<field_with_ships>,<field_without_ships>\n> "
                command = input(prompt)
                if command not in ["field_with_ships", "field_without_ships"]:
                    x, y = command.strip().split()
                    assert 11 > int(y) > 0
                    x, y = int(y) - 1, "abcdefghij".index(x)
                    return x, y
                else:
                    mode = 1 if command == "field_with_ships" else 2
                    return mode
            except ValueError:
                print("Input two coordinates separated by space")
                continue
            except (IndexError, AssertionError):
                print("Input two coordinates : x and y \nx from \'a\' to \'i\', y from 1 to 10")
                continue
