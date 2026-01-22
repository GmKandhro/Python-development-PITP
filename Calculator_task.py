while(True):
    num1 = int(input("Enter First number::> "))
    num2 = int(input("Enter second number::> "))

    operator = input("What do you want to perform: (+ , - , * , / , % , ** , //)")

    if(operator == "+"):
        print(f"{num1} + {num2} is: {num1 + num2}")
    elif(operator == "-"):
        print(f"{num1} - {num2} is: {num1 - num2}")
    elif(operator == "*"):
        print(f"{num1} * {num2} is: {num1 * num2}")
    elif(operator == "/"):
        print(f"{num1} / {num2} is: {num1 / num2}")
    elif(operator == "%"):
        print(f"{num1} % {num2} is: {num1 % num2}")
    elif(operator == "**"):
        print(f"{num1} power {num2} is: {num1 ** num2}")
    else:
        print(f"{num1} floor division {num2} is: {num1 // num2}")
    moreOprations = input("Do you want to perform more operations (yes/no) :> ")
    if(moreOprations == "no"):
        break