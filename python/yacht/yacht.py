YACHT                   = lambda x: yacht(x)
ONES                    = lambda x: multiples(x, 1)
TWOS                    = lambda x: multiples(x, 2)
THREES                  = lambda x: multiples(x, 3)
FOURS                   = lambda x: multiples(x, 4)
FIVES                   = lambda x: multiples(x, 5)
SIXES                   = lambda x: multiples(x, 6)
FULL_HOUSE              = lambda x: full_house(x)
FOUR_OF_A_KIND          = lambda x: four_of_a_kind(x)
LITTLE_STRAIGHT         = lambda x: little_straight(x)
BIG_STRAIGHT            = lambda x: big_straight(x)
CHOICE                  = lambda x: sum(x)


def multiples(dice, num):
    return dice.count(num)*num


def yacht(dice):
    if len(set(dice)) == 1:
        return 50
    return 0


def full_house(dice):
    for num in dice:
        count = dice.count(num)
        if count in [2,3]:
            continue
        return 0
    return sum(dice)


def four_of_a_kind(dice):
    for num in dice:
        count = dice.count(num)
        if count in [4,5]:
            return num*4
    return 0


def straight(dice):
    for i, num in enumerate(dice[:-1]):
        if num+1 != dice[i+1]:
            return 0
    return 30


def little_straight(dice):
    dice.sort()
    if dice[0] == 1:
        return straight(dice)
    return 0


def big_straight(dice):
    dice.sort()
    if dice[0] == 2:
        return straight(dice)
    return 0


def score(dice, category):
    return category(dice)
