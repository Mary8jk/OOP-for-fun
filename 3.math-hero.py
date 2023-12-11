# в разработке
from datetime import time


class Hero:
    def __init__(self, name):
        self.name = name
        self.choice = None

    def choose(self):
        a = 
        b =
        res = a * b
        self.choice = input(f"{self.name}, введи результат "
                            f"{a}*{b}= ").lower()

    def get_winner(self):
        if self.player.choice == self.player2.choice: #если не правильно введено число
            return None
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
