class Game:

    def __init__(self):
        self.wins =0
        self.loses =0

    def won_level(self):
        self.wins +=1

    def lose_level(self):
        self.loses -=1


    @property
    def score(self):
        return self.wins + self.loses

g = Game()
print("wins {} , loses {}".format(g.wins ,g.loses))
g.won_level()
g.won_level()
g.won_level()
g.lose_level()
print("Score ->",g.score)