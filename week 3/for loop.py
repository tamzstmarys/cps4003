import random

cables_to_avoid = int(input("How many live cables must I avoid: "))

avoided_cables = 0

while True:
    is_live_cable = random.choice([True, False])

    if is_live_cable:
        print("Avoid live cable")
        avoided_cables += 1

    if avoided_cables == cables_to_avoid:
       break