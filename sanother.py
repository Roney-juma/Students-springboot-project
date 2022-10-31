for n in range(3):
    while True:
        i = input("Please enter a six digit integer:")
        if i.isnumeric():
            if len(i)==6:
                i_integer = int(i)
                print("Your number is:",i_integer,"and the data type is:",type(i_integer))
        break
    else:
        print("Enter value is not numeric") 