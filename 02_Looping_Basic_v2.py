# checks that users enter a number that is  ore than zero
valid = False
while not valid:

    error = "please enter a number that is more than zero"

    try:

        # ask user to enter a number
        response = float(input("enter a number: "))

        # checks number is more than zero
        if response > 0:
            valid = True

        # outputs error if input is invalid
        else:
            print(error)
            print()

    except ValueError:
        print(error)