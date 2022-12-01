

def main():

    clubs = ['1_c', '2_c', '3_c', '4_c', '5_c', '6_c', '7_c', '8_c',
             '9_c', '10_c', '11_c', '12_c', '13_c', '14_c', '15_c']

    hearts = ['1_h', '2_h', '3_h', '4_h', '5_h', '6_h', '7_h',
              '8_h', '9_h', '10_h', '11_h', '12_h', '13_h', '14_h', '15_h']

    spades = ['1_s', '2_s', '3_s', '4_s', '5_s', '6_s', '7_s',
              '8_s', '9_s', '10_s', '11_s', '12_s', '13_s', '14_s', '15_s']

    diamond = ['1_d', '2_d', '3_d', '4_d', '5_d', '6_d', '7_d',
               '8_d', '9_d', '10_d', '11_d', '12_d', '13_d', '14_d', '15_d']

    jokers = ["RED_J", "BLACK_J"]

    cards = clubs + hearts + spades + diamond + jokers

    print(cards)


if __name__ == "__main__":
    main()
