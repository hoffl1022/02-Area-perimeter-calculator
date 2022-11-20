# functions go here

# checks input is a number more than zero
def num_check(question):
    valid = False
    while not valid:

        error = "please enter a number that is more than zero"

        try:

            # ask user to enter a number
            response = float(input(question))

            # checks number is more than zero
            if response > 0: 
                return response

            # outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error)



# main routine goes here
width = num_check("Width: ")
height = num_check("Height: ")

# calculate area (width x height)
area = width * height

# calculate perimeter (width + height) x 2
perimeter = 2 * (width + height)

# output area and perimeter
print("Area: {} square units".format(area))
print("Perimeter: {} units".format(perimeter))