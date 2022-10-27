# checks that users enter a number that is more than zero

def num_check(question):
    valid = False
    while not valid:

         error = "Please enter a number that is ,more than zero"

         try:

            # ask a user to enter a number
            response = float(input("Enter a number: "))

            # checks number is more than zero
            if response > 0:
               return response

            # outputs error if input ius invalid
            else:
              print(error)
            print()
 
         except ValueError:
          print(error)



width = num_check("what is the width?")
height = num_check("what is the height?")

print()
print("the width is",width)
print("The height is", height)

