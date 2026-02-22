positive = 0
negative = 0 
zeroes = 0

while True:
    inp = input("Enter a number:- ")
    if inp == "done":
        break

    try:
        float_inp = float(inp)
    except:
        print("Error!. Enter a valid input")

    if float_inp > 0:
        positive += 1
    elif float_inp < 0:
        negative += 1
    elif float_inp == 0:
        zeroes += 1;


print("!-------Detailed Summary--------!")
print("The number of positive numbers are:-  ", positive)
print("The number of negative numbers are:- ", negative)
print("The number of numbers that are zero" , zeroes)