class Player:
    def __init__(self, name):
        self.name = name
        self.choice = None

    def choose(self):
        self.choice = input(f"{self.name}, choose rock, paper "
                            f"or scissors: ").lower()


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.rules = {
            "rock": "scissors",
            "paper": "rock",
            "scissors": "paper"
        }

    def get_winner(self):
        if self.player1.choice == self.player2.choice:
            return None
        elif self.rules[self.player1.choice] == self.player2.choice:
            return self.player1
        else:
            return self.player2

    def play(self):
        self.player1.choose()
        self.player2.choose()
        winner = self.get_winner()
        if winner:
            print(f"{winner.name} победил!")
        else:
            print("У нас ничья.")


# Пример использования
player1 = Player("Игрок 1")
player2 = Player("Игрок 2")
game = Game(player1, player2)
game.play()
