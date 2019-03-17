from game import Game
print("Welcome to my BattleShip game")
print("Enjoy it")
g = Game()
while True:
    if g.player_win():
        break
    g.read_position()
