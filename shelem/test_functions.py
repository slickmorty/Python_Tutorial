import random


def shuffle(cards: list) -> list:

    random.shuffle(cards)
    return cards


def main():
    a = [1, 2, 3, 4, 5, 6, 7]
    print(a)

    print(shuffle(a))


if __name__ == "__main__":
    main()
