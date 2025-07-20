num1 = int(input("enter the first number: "))
num2 = int(input("enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        print(f"the result is {num1 + num2}")
    case "-":
        print(f"the result is {num1 - num2}")
    case "/":
        if num2 == 0:
            print("cannot divide by zero")
        else:
            print(f"the result is {float(num1 / num2)}")
    case "-":
        print(f"the result is {num1 + num2}")
    case _:
        print("invalid operation")
