while True:
    input1=input("Operation: ")
    a=float(input("what is your first number:"))
    b=float(input("what is your second number:"))
    if input1 == "+" :
        print(a+b)
    elif input1 == "-":
        print(a-b)
    elif input1 == "*":
        print(a*b)
    elif input1 == "/":
        print(a/b)
    elif input1 == "**":
        print(a**b)
