ch = input("Please enter any character excpet 'q' to continue: ")
while (ch != "q"):
    userInput1 = input("enter the string: ")
    userInput2 = input("enter the string to search: ")

    if userInput2 in userInput1:
        print("subsstring present")
    else:
        print("not found")
    print("***************************************")
    ch = input("Enter 'q' to quit and 'p' to proceed: ")
print("***************************************")
print("Thankyou for trying to execute the code...")
print("***************************************")
