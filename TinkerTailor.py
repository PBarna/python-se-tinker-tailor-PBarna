
class TinkerTailor:

    def __init__(self, number, step):
        self.players = []
        self.result = []
        self.number = number + 1
        self.step = step - 1
        self.position = self.step

    def pick(self):
        if n > s:
            picked = self.players.pop(self.position)
            self.result.append(picked)
        else:
            print("Please read the rules of the game")
            TinkerTailor(int(n), int(s))


    def setup(self):
        for i in range(1,self.number):
            self.players.append(i)

    def game(self):
        while len(self.players) > 0:
            self.pick()
            if self.players:
                self.position = (self.position + self.step) % len(self.players)


if __name__ == '__main__':
    n, s = input('Enter the number of people: '), input('Enter the number of steps: ')
    tinker = TinkerTailor(int(n), int(s))
    tinker.setup()
    tinker.game()
    print("The result: ", tinker.result)
