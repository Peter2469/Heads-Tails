import random
import time
import sys

class Entity:
    def __init__(self, name:str):
        self.lives = 5
        self.name = name

    def turn_logic(self, choice: str):
        heads_tails = random.choice(["heads", "tails"])
        if heads_tails == choice:
            print(f"It landed on *{choice}* which means you were correct!\n")
        else:
            print(f"You were not correct as it was {heads_tails}!\n")
            self.lives -= 1
            self.check_lives()
        
    def check_lives(self):
        if self.lives == 0:
            print(f"{self.name} has no more lives!")
            sys.exit()

class Dealer(Entity):
    def __init__(self, name="Dealer"):
        super().__init__(name)

    def do_turn(self):
        self.check_lives()
        heads_tails = random.choice(["heads", "tails"])
        print(f"{self.name} has {self.lives} lives left")
        print(f"{self.name}: I think it will be {heads_tails}!")
        self.turn_logic(heads_tails)

class Player(Entity):
    def do_turn(self):
        self.check_lives()
        print(f"{self.name} has {self.lives} lives left")
        data = input("Do you think it will be Heads or Tails?\n").lower()
        self.turn_logic(data)

player = Player("Player")
dealer = Dealer()

while True:
    player.do_turn()

    time.sleep(2)

    dealer.do_turn()

    time.sleep(2)
