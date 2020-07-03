try:
    while True:
        num1 = input("Enter number : ")
        num2 = input("Enter number : ")
        addition = int(num1) + int(num2)
        print(addition)
except ValueError as error:
   print("you Are defining String")
