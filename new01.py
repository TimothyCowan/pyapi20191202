#!/usr/bin/python3

class MarioKartPlayer:
import json

    def __init__(self, name, karttype):
        with open ('mkcharacters.json') as mkd:
            stats = json.load()
        self.name = name  # name of character player
        self.karttype = karttype  # kart selected
        self.score = 0  # current core
        self.item = None  # item character has picked up
        self.type = stats[name]["type"]
    # display when object is printed
    def __str__(self):
        return self.name

    #method to change score
    def scorechange(self, condition):
        if condition == "coin":
            self.score += 10
        elif condition == "finishline":
            self.score += 25
        else:
            self.score += 5


def main():
    print("Classes w/ mario kart")
    player1 = MarioKartPlayer("Yoshi", "50cc")
    print(player1.name)
    print(player1.karttype)
    print(player1.score)
    print(player1.item)
    player1.scorechange('test')
    player1.scorechange('finishline')
    player1.scorechange('coin')
    print(player1.score)

if __name__ == "__main__":
    main()
