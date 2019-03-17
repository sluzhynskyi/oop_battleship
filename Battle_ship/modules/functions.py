import string

alphabet = string.ascii_lowercase


def read_field(path):
    """
    Reads from txt to csv file
    :param path: str
    :return: None
    """
    with open(path, "r", encoding="utf8") as file:
        with open(path[:-4] + ".csv", "w+", encoding="utf8") as out_file:
            for line in file:
                for ch in line:
                    if ch == "*":
                        out_file.write("1,")
                    elif ch == " ":
                        out_file.write("0,")
                out_file.write("\n")


def has_ship(path, position):
    """

    :param path:
    :param position: tuple  (int, str)
    :return: bool
    """
    x, y = position
    with open(path, "r", encoding="utf8") as file:
        file = file.readlines()
        if file[alphabet.index(y)].split(",")[x - 1] == "1":
            return True
        return False


def ship_size(path, position):
    """
    :param path: str
    :param position: tuple (int, str)
    :return: int
    """
    x, y = position[0] - 1, position[1]

    k, c, l, n = 1, 1, 1, 1
    with open(path, "r", encoding="utf8") as file:
        file = file.readlines()
        for i in file:
            i.split(",")
        lst_field = [i.split(",") for i in file if i != "\n"]
    if has_ship(path, position):
        # Checking if ship is on x direction
        while 10 > x + k > -1 \
                and lst_field[alphabet.index(y)][x + k] == "1":
            k += 1
        while 10 > x - c > -1 \
                and lst_field[alphabet.index(y)][x - c] == "1":
            c += 1
        # Checking if ship is on y direction
        while 10 > alphabet.index(y) + l > -1 \
                and lst_field[alphabet.index(y) + l][x] == "1":
            l += 1
        while 10 > alphabet.index(y) - n > -1 \
                and lst_field[alphabet.index(y) - n][x] == "1":
            n += 1
        return k + c + l + n - 3
    else:
        return 0
