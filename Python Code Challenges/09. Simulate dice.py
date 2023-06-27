import random

def throwDice(*dices):
    dict = {}
    for x in range(1000000):
        sum = 0
        for dice in dices:
            sum += random.randint(1, dice)
        dict.update({sum: dict.get(sum, 0) + 1})
    sums = list(dict.keys())
    sums.sort()
    print("\nOUTCOME PROBABILITY")
    for sum in sums:
        print(str(sum) + "\t" + str(round(dict.get(sum) / 1000000 * 100, 2)) + "%")

throwDice(4, 6, 6)