import random


def shuffle(cards: list) -> None:

    random.shuffle(cards)
    return None


def pre_hokm_dist(cards: list, players: list) -> None:
    for player in players:
        for _ in range(4):
            player.append(cards.pop(0))

    return None


def main():

    cards = {"clubs": ['2_c', '3_c', '4_c', '5_c', '6_c', '7_c', '8_c',
                       '9_c', '10_c', '11_c', '12_c', '13_c', '14_c'],
             "diamond": ['2_d', '3_d', '4_d', '5_d', '6_d', '7_d',
                         '8_d', '9_d', '10_d', '11_d', '12_d', '13_d', '14_d'],
             "spades": ['2_s', '3_s', '4_s', '5_s', '6_s', '7_s',
                        '8_s', '9_s', '10_s', '11_s', '12_s', '13_s', '14_s'],
             "hearts": ['2_h', '3_h', '4_h', '5_h', '6_h', '7_h',
                        '8_h', '9_h', '10_h', '11_h', '12_h', '13_h', '14_h'],
             "jokers": ["RED_J", "BLACK_J"]
             }

    cards_list = cards['clubs']+cards['diamond'] + \
        cards['hearts']+cards['jokers']+cards['spades']

    players: dict = {"player_1": {"player_cards": [], "points": [], "is_hakem": False},
                     "player_2": {"player_cards": [], "points": [], "is_hakem": False},
                     "player_3": {"player_cards": [], "points": [], "is_hakem": False},
                     "player_4": {"player_cards": [], "points": [], "is_hakem": False}}

    hakem = "player_1"


if __name__ == "__main__":
    main()


# pass by value and refrence
"""def add(z, k):

    z.append(1)
    k.append(2)
    return z+k


x = [9, 4, 5]
y = [10, 11, 12]

z = add(x, y)

print(z)

print(x)
print(y)"""
