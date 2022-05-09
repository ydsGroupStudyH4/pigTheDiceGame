def roll_and_stop():
    roll_or_stop = 0
    while int(input("Press 1(Roll) or 0(Stop) : ")) == 1:
        print("again")
    return roll_or_stop


print(roll_and_stop())
