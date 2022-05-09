def make_n_persons():
    while True:
        n= int(input('Please set the number of people'))
        if n>0:
            if n>4:
                print("Please set the number under 4")
            else:
                print(f"The number of people is: {n}")
                return n
        else:
            print("you typed wrong number, please do it again.")

def roll_and_stop():
    roll_or_stop = 0
    while int(input("Press 1(Roll) or 0(Stop) : ")) == 1:
        print("again")
    return roll_or_stop


print(roll_and_stop())

