
# checks that users enter a number that is more than zero
def num_check(question):
    valid = False
    while not valid:

         error = "Please enter a number that is ,more than zero"

         try:

            # ask a user to enter a number
            response = float(input(question))

            # checks number is more than zero
            if response > 0:
               return response

            # outputs error if input ius invalid
            else:
              print(error)
            print()
 
         except ValueError:
          print(error)

print()
print("*** area perimeter calculator ****")
print()

keep_going = ""
while keep_going == "":

    # get width and height, check they are more than zero (using number checking function)
    width = num_check("width: ")
    height = num_check("height: ")

    # calculate area and perimeter
    area = width * height

    perimeter= 2 * (width + height)

    # Output answer, format to 2dp
    print("perimeter {:.2f} units" .format(perimeter))
    print("area: {:.2f} square units" .format(area))
    print()

    keep_going = input("press <enter> to keep going or any key to quit")

print()
print("Thanks for using the area / perimeter calculator")