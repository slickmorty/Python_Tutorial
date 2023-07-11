import random

hand: str = random.choice(["right", "left"])
selected_hand: str = input("Enter right or left: ")
if selected_hand == hand:
    print("You won")
elif selected_hand != hand:
    print("You lost")

# if condition:
#   dastoor1
#   dastoor2
#   ........
# elif condition:
#   dastoorat
# elif condition:
#   dastoorat
# ...............
# else:
#   dastoorat
